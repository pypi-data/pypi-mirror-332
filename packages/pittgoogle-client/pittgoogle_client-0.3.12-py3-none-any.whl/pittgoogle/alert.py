# -*- coding: UTF-8 -*-
"""Classes for working with astronomical alerts.

.. autosummary::

    Alert

----
"""
import base64
import datetime
import io
import logging
import random
from pathlib import Path
from typing import TYPE_CHECKING, Any, Mapping, Union

import attrs
import google.cloud.pubsub_v1

from . import exceptions, registry, types_
from .schema import (
    Schema,  # so 'schema' module doesn't clobber 'Alert.schema' attribute
)

if TYPE_CHECKING:
    import astropy.table
    import google.cloud.functions_v1
    import pandas as pd  # always lazy-load pandas. it hogs memory on cloud functions and run

LOGGER = logging.getLogger(__name__)


@attrs.define(kw_only=True)
class Alert:
    """Container for an astronomical alert.

    To create an `Alert`, use one of the `from_*` methods like :meth:`pittgoogle.Alert.from_dict`.
    Instances of this class are also returned by other calls like :meth:`pittgoogle.pubsub.Subscription.pull_batch`.

    Args:
        dict (dict, optional):
            The alert data as a dictionary. If not provided, it will be loaded from the
        attributes (dict, optional):
            Attributes or custom metadata for the alert.
        schema_name (str):
            Name of the schema for the alert. This is use to deserialize the alert bytes.
            See :meth:`pittgoogle.registry.Schemas.names` for a list of options.
            If not provided, some properties of the `Alert` may not be available.
        msg (PubsubMessageLike or google.cloud.pubsub_v1.types.PubsubMessage, optional):
            The incoming Pub/Sub message object. This class is documented at
            `<https://cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.PubsubMessage>`__.
        path (pathlib.Path, optional):
            Path to a file containing the alert data.

    ----
    """

    _dict: Mapping | None = attrs.field(default=None)
    _attributes: Mapping[str, str] | None = attrs.field(default=None)
    schema_name: str | None = attrs.field(default=None)
    msg: google.cloud.pubsub_v1.types.PubsubMessage | types_.PubsubMessageLike | None = (
        attrs.field(default=None)
    )
    path: Path | None = attrs.field(default=None)
    # Use "Union" because " | " is throwing an error when combined with forward references.
    context: Union[
        "google.cloud.functions_v1.context.Context", types_._FunctionsContextLike, None
    ] = attrs.field(default=None)
    _dataframe: Union["pd.DataFrame", None] = attrs.field(default=None)
    _skymap: Union["astropy.table.Qtable", None] = attrs.field(default=None)
    _schema: Schema | None = attrs.field(default=None, init=False)

    # ---- class methods ---- #
    @classmethod
    def from_cloud_functions(
        cls,
        event: Mapping,
        context: "google.cloud.functions_v1.context.Context",
        schema_name: str | None = None,
    ):
        """Create an `Alert` from an 'event' and 'context', as received by a Cloud Functions module.

        Argument definitions copied from https://cloud.google.com/functions/1stgendocs/tutorials/pubsub-1st-gen

        Args:
            event (dict):
                The dictionary with data specific to this type of event. The `@type` field maps to
                `type.googleapis.com/google.pubsub.v1.PubsubMessage`. The `data` field maps to the
                PubsubMessage data in a base64-encoded string. The `attributes` field maps to the
                PubsubMessage attributes if any is present.
            context (google.cloud.functions.Context):
                Metadata of triggering event including `event_id` which maps to the PubsubMessage
                messageId, `timestamp` which maps to the PubsubMessage publishTime, `event_type` which
                maps to `google.pubsub.topic.publish`, and `resource` which is a dictionary that
                describes the service API endpoint pubsub.googleapis.com, the triggering topic's name,
                and the triggering event type `type.googleapis.com/google.pubsub.v1.PubsubMessage`.
        """
        return cls(
            msg=types_.PubsubMessageLike(
                # data is required. the rest should be present in the message, but use get to be lenient
                data=base64.b64decode(event["data"]),
                attributes=event.get("attributes", {}),
                message_id=context.event_id,
                publish_time=cls._str_to_datetime(context.timestamp),
            ),
            context=context,
            schema_name=schema_name,
        )

    @classmethod
    def from_cloud_run(cls, envelope: Mapping, schema_name: str | None = None) -> "Alert":
        """Create an `Alert` from an HTTP request envelope containing a Pub/Sub message, as received by a Cloud Run module.

        Args:
            envelope (dict):
                The HTTP request envelope containing the Pub/Sub message.
            schema_name (str, optional):
                The name of the schema to use. Defaults to None.

        Returns:
            Alert:
                An instance of the `Alert` class.

        Raises:
            BadRequest:
                If the Pub/Sub message is invalid or missing.

        Example:

            Code for a Cloud Run module that uses this method to open a ZTF alert:

            .. code-block:: python

                import pittgoogle
                # flask is used to work with HTTP requests, which trigger Cloud Run modules
                # the request contains the Pub/Sub message, which contains the alert packet
                import flask

                app = flask.Flask(__name__)

                # function that receives the request
                @app.route("/", methods=["POST"])
                def index():

                    try:
                        # unpack the alert
                        # if the request does not contain a valid message, this raises a `BadRequest`
                        alert = pittgoogle.Alert.from_cloud_run(envelope=flask.request.get_json(), schema_name="ztf")

                    except pittgoogle.exceptions.BadRequest as exc:
                        # return the error text and an HTTP 400 Bad Request code
                        return str(exc), 400

                    # continue processing the alert
                    # when finished, return an empty string and an HTTP success code
                    return "", 204
        """
        # check whether received message is valid, as suggested by Cloud Run docs
        if not envelope:
            raise exceptions.BadRequest("Bad Request: no Pub/Sub message received")
        if not isinstance(envelope, dict) or "message" not in envelope:
            raise exceptions.BadRequest("Bad Request: invalid Pub/Sub message format")

        return cls(
            msg=types_.PubsubMessageLike(
                # data is required. the rest should be present in the message, but use get to be lenient
                data=base64.b64decode(envelope["message"]["data"].encode("utf-8")),
                attributes=envelope["message"].get("attributes", {}),
                message_id=envelope["message"].get("message_id"),
                publish_time=cls._str_to_datetime(envelope["message"]["publish_time"]),
                ordering_key=envelope["message"].get("ordering_key"),
            ),
            schema_name=schema_name,
        )

    @classmethod
    def from_dict(
        cls,
        payload: Mapping,
        attributes: Mapping[str, str] | None = None,
        schema_name: str | None = None,
    ) -> "Alert":
        """Create an `Alert` object from the given `payload` dictionary.

        Args:
            payload (dict):
                The dictionary containing the data for the `Alert` object.
            attributes (Mapping[str, str], None):
                Additional attributes for the `Alert` object. Defaults to None.
            schema_name (str, None):
                The name of the schema. Defaults to None.

        Returns:
            Alert:
                An instance of the `Alert` class.
        """
        return cls(dict=payload, attributes=attributes, schema_name=schema_name)

    @classmethod
    def from_msg(
        cls, msg: "google.cloud.pubsub_v1.types.PubsubMessage", schema_name: str | None = None
    ) -> "Alert":
        """Create an `Alert` object from a `google.cloud.pubsub_v1.types.PubsubMessage`.

        Args:
            msg (google.cloud.pubsub_v1.types.PubsubMessage):
                The PubsubMessage object to create the Alert from.
            schema_name (str, optional):
                The name of the schema to use for the Alert. Defaults to None.

        Returns:
            Alert:
                The created `Alert` object.
        """
        return cls(msg=msg, schema_name=schema_name)

    @classmethod
    def from_path(cls, path: str | Path, schema_name: str | None = None) -> "Alert":
        """Create an `Alert` object from the file at the specified `path`.

        Args:
            path (str or Path):
                The path to the file containing the alert data.
            schema_name (str, optional):
                The name of the schema to use for the alert. Defaults to None.

        Returns:
            Alert:
                An instance of the `Alert` class.

        Raises:
            FileNotFoundError:
                If the file at the specified `path` does not exist.
            IOError:
                If there is an error reading the file.
        """
        with open(path, "rb") as f:
            bytes_ = f.read()
        return cls(
            msg=types_.PubsubMessageLike(data=bytes_), schema_name=schema_name, path=Path(path)
        )

    def to_mock_input(self, cloud_functions: bool = False):
        if not cloud_functions:
            raise NotImplementedError("Only cloud functions has been implemented.")
        return MockInput(alert=self).to_cloud_functions()

    # ---- properties ---- #
    @property
    def attributes(self) -> Mapping:
        """Return the alert's custom metadata.

        If this was not provided (typical case), this attribute will contain a copy of
        the incoming :attr:`Alert.msg.attributes`.

        You may update this dictionary as desired. If you publish this alert using
        :attr:`pittgoogle.Topic.publish`, this dictionary will be sent as the outgoing
        message's Pub/Sub attributes.
        """
        if self._attributes is None:
            if self.msg is not None:
                self._attributes = dict(self.msg.attributes)
            else:
                self._attributes = {}
            self._add_id_attributes()
        return self._attributes

    @property
    def dict(self) -> Mapping:
        """Alert data as a dictionary.

        If this was not provided (typical case), this attribute will contain the deserialized
        alert bytes from :attr:`Alert.msg.data`.

        You may update this dictionary as desired. If you publish this alert using
        :attr:`pittgoogle.Topic.publish`, this dictionary will be sent as the outgoing
        Pub/Sub message's data payload.

        Returns:
            dict:
                The alert data as a dictionary.

        Raises:
            SchemaError:
                If unable to deserialize the alert bytes.
        """
        if self._dict is None:
            self._dict = self.schema.deserialize(self.msg.data)
        return self._dict

    @property
    def dataframe(self) -> "pd.DataFrame":
        """Return a pandas DataFrame containing the source detections."""
        if self._dataframe is not None:
            return self._dataframe

        import pandas as pd  # always lazy-load pandas. it hogs memory on cloud functions and run

        # sources and previous sources are expected to have the same fields
        sources_df = pd.DataFrame([self.get("source")] + self.get("prv_sources", []))
        # sources and forced sources may have different fields
        forced_df = pd.DataFrame(self.get("prv_forced_sources", []))

        # use nullable integer data type to avoid converting ints to floats
        # for columns in one dataframe but not the other
        sources_ints = [c for c, v in sources_df.dtypes.items() if v == int]
        sources_df = sources_df.astype(
            {c: "Int64" for c in set(sources_ints) - set(forced_df.columns)}
        )
        forced_ints = [c for c, v in forced_df.dtypes.items() if v == int]
        forced_df = forced_df.astype(
            {c: "Int64" for c in set(forced_ints) - set(sources_df.columns)}
        )

        self._dataframe = pd.concat([sources_df, forced_df], ignore_index=True)
        return self._dataframe

    @property
    def alertid(self) -> str | int:
        """Return the alert ID. Convenience wrapper around :attr:`Alert.get`.

        If the survey does not define an alert ID, this returns the `sourceid`.
        """
        return self.get("alertid", self.sourceid)

    @property
    def objectid(self) -> str | int:
        """Return the object ID. Convenience wrapper around :attr:`Alert.get`.

        The "object" represents a collection of sources, as determined by the survey.
        """
        return self.get("objectid")

    @property
    def sourceid(self) -> str | int:
        """Return the source ID. Convenience wrapper around :attr:`Alert.get`.

        The "source" is the detection that triggered the alert.
        """
        return self.get("sourceid")

    @property
    def schema(self) -> Schema:
        """Return the schema from the :class:`pittgoogle.registry.Schemas` registry.

        Raises:
            SchemaError:
                If the `schema_name` is not supplied or a schema with this name is not found.
        """
        if self._schema is None:
            self._schema = registry.Schemas.get(self.schema_name)
        return self._schema

    @property
    def skymap(self) -> Union["astropy.table.QTable", None]:
        """Alert skymap as an astropy Table. Currently implemented for LVK schemas only.

        This skymap is loaded from the alert to an astropy table and extra columns are added, following
        https://emfollow.docs.ligo.org/userguide/tutorial/multiorder_skymaps.html.
        The table is sorted by PROBDENSITY and then UNIQ, in descending order, so that the most likely
        location is first. Columns:

            - UNIQ: HEALPix pixel index in the NUNIQ indexing scheme.
            - PROBDENSITY: Probability density in the pixel (per steradian).
            - nside: HEALPix nside parameter defining the pixel resolution.
            - ipix: HEALPix pixel index at resolution nside.
            - ra: Right ascension of the pixel center (radians).
            - dec: Declination of the pixel center (radians).
            - pixel_area: Area of the pixel (steradians).
            - prob: Probability density in the pixel.
            - cumprob: Cumulative probability density up to the pixel.

        Examples:

            .. code-block:: python

                # most likely location
                alert.skymap[0]

                # 90% credible region
                alert.skymap[:alert.skymap['cumprob'].searchsorted(0.9)]
        """
        if self._skymap is None and self.schema_name.startswith("lvk"):
            import astropy.table
            import astropy.units
            import hpgeom
            import numpy as np

            if self.get("skymap") is None:
                return

            skymap = astropy.table.QTable.read(io.BytesIO(base64.b64decode(self.get("skymap"))))
            skymap.sort(["PROBDENSITY", "UNIQ"], reverse=True)

            skymap["nside"] = (2 ** (np.log2(skymap["UNIQ"] // 4) // 2)).astype(int)
            skymap["ipix"] = skymap["UNIQ"] - 4 * skymap["nside"] ** 2

            skymap["ra"], skymap["dec"] = hpgeom.pixel_to_angle(
                skymap["nside"], skymap["ipix"], degrees=False
            )
            skymap["ra"].unit = astropy.units.rad
            skymap["dec"].unit = astropy.units.rad

            skymap["pixel_area"] = hpgeom.nside_to_pixel_area(skymap["nside"], degrees=False)
            skymap["pixel_area"].unit = astropy.units.sr

            skymap["prob"] = skymap["pixel_area"] * skymap["PROBDENSITY"]
            skymap["cumprob"] = skymap["prob"].cumsum()

            self._skymap = skymap

        return self._skymap

    # ---- methods ---- #
    def _add_id_attributes(self) -> None:
        """Add the IDs ("alertid", "objectid", "sourceid") to :attr:`Alert.attributes`."""
        ids = ["alertid", "objectid", "sourceid"]
        values = [self.get(id) for id in ids]

        # get the survey-specific field names
        survey_names = [self.get_key(id) for id in ids]
        # if the field is nested, the key will be a list
        # but pubsub message attributes must be strings. join to avoid a future error on publish
        names = [".".join(id) if isinstance(id, list) else id for id in survey_names]

        # only add to attributes if the survey has defined this field and it's not already in the attributes
        for idname, idvalue in zip(names, values):
            if idname is not None and idname not in self._attributes:
                self._attributes[idname] = idvalue

    def get(self, field: str, default: Any = None) -> Any:
        """Return the value of a field from the alert data.

        Parameters:
            field (str):
                Name of a field. This must be one of the generic field names used by Pitt-Google
                (keys in :attr:`Alert.schema.map`). To use a survey-specific field name instead, use
                :attr:`Alert.dict.get`.
            default (str, optional):
                The default value to be returned if the field is not found.

        Returns:
            any:
                The value in the :attr:`Alert.dict` corresponding to the field.
        """
        survey_field = self.schema.map.get(field)  # str, list[str], or None

        if survey_field is None:
            return default

        if isinstance(survey_field, str):
            return self.dict.get(survey_field, default)

        # if survey_field is not one of the expected types, the schema map is malformed
        # maybe this was intentional, but we don't know how to handle it here
        if not isinstance(survey_field, list):
            raise TypeError(
                f"field lookup not implemented for a schema-map value of type {type(survey_field)}"
            )

        # the list must have more than 1 item, else it would be a single str
        if len(survey_field) == 2:
            try:
                return self.dict[survey_field[0]][survey_field[1]]
            except (KeyError, TypeError):
                return default

        if len(survey_field) == 3:
            try:
                return self.dict[survey_field[0]][survey_field[1]][survey_field[2]]
            except (KeyError, TypeError):
                return default

        raise NotImplementedError(
            f"field lookup not implemented for depth {len(survey_field)} (key = {survey_field})"
        )

    def get_key(
        self, field: str, name_only: bool = False, default: str | None = None
    ) -> str | list[str] | None:
        """Return the survey-specific field name.

        Args:
            field (str):
                Generic field name whose survey-specific name is to be returned. This must be one of the
                keys in the dict `self.schema.map`.
            name_only (bool):
                In case the survey-specific field name is nested below the top level, whether to return
                just the single final name as a str (True) or the full path as a list[str] (False).
            default (str or None):
                Default value to be returned if the field is not found.

        Returns:
            str or list[str]):
                Survey-specific name for the `field`, or `default` if the field is not found.
                list[str] if this is a nested field and `name_only` is False, else str with the
                final field name only.
        """
        survey_field = self.schema.map.get(field)  # str, list[str], or None

        if survey_field is None:
            return default

        if name_only and isinstance(survey_field, list):
            return survey_field[-1]

        return survey_field

    def _prep_for_publish(self) -> tuple[bytes, Mapping[str, str]]:
        """Serialize the alert dict and convert all attribute keys and values to strings."""
        message = self.schema.serialize(self.drop_cutouts())
        # Pub/Sub requires attribute keys and values to be strings. Sort the keys while we're at it.
        attributes = {str(key): str(self.attributes[key]) for key in sorted(self.attributes)}
        return message, attributes

    def drop_cutouts(self) -> dict:
        """Drop the cutouts from the alert dictionary.

        Returns:
            dict:
                The `dict` with the cutouts (postage stamps) removed.
        """
        cutouts = [
            self.get_key(key) for key in ["cutout_difference", "cutout_science", "cutout_template"]
        ]
        alert_stripped = {k: v for k, v in self.dict.items() if k not in cutouts}
        return alert_stripped

    @staticmethod
    def _str_to_datetime(str_time: str) -> datetime.datetime:
        # occasionally the string doesn't include microseconds so we need a try/except
        try:
            return datetime.datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%S.%f%z")
        except ValueError:
            return datetime.datetime.strptime(str_time, "%Y-%m-%dT%H:%M:%S%z")


@attrs.define
class MockInput:
    alert: Alert = attrs.field()

    def to_cloud_functions(self) -> tuple[dict, types_._FunctionsContextLike]:
        """

        Parameter definitions copied from https://cloud.google.com/functions/1stgendocs/tutorials/pubsub-1st-gen

        Returns:
            event (dict):
                The dictionary with data specific to this type of event. The `@type` field maps to
                `type.googleapis.com/google.pubsub.v1.PubsubMessage`. The `data` field maps to the
                PubsubMessage data in a base64-encoded string. The `attributes` field maps to the
                PubsubMessage attributes if any is present.
            context (google.cloud.functions.Context):
                Metadata of triggering event including `event_id` which maps to the PubsubMessage
                messageId, `timestamp` which maps to the PubsubMessage publishTime, `event_type` which
                maps to `google.pubsub.topic.publish`, and `resource` which is a dictionary that
                describes the service API endpoint pubsub.googleapis.com, the triggering topic's name,
                and the triggering event type `type.googleapis.com/google.pubsub.v1.PubsubMessage`.
        """
        message, attributes = self.alert._prep_for_publish()
        event_type = "type.googleapis.com/google.pubsub.v1.PubsubMessage"
        now = (
            datetime.datetime.now(datetime.timezone.utc)
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z")
        )

        event = {"@type": event_type, "data": base64.b64encode(message), "attributes": attributes}

        context = types_._FunctionsContextLike(
            event_id=str(int(1e12 * random.random())),
            timestamp=now,
            event_type="google.pubsub.topic.publish",
            resource={
                "name": "projects/NONE/topics/NONE",
                "service": "pubsub.googleapis.com",
                "type": event_type,
            },
        )

        return event, context
