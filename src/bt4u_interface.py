from dataclasses import dataclass
from datetime import datetime
from http.client import HTTPException
from typing import Any

import requests
import xmltodict


@dataclass
class BT4U_Interface:
    """
    A class for interfacing with the BT4U API to get information on buses and routes.

    :author: Barrett Wise
    :date: 1/22/25
    :var _BASE_URL: The URL of the website hosting the API.
    """

    _BASE_URL = "http://216.252.195.248/webservices/bt4u_webservice.asmx/"

    @classmethod
    def check_for_known_place(cls, place_name: str = "") -> dict[str, Any]:
        """
        Get information on a known place.

        :param place_name: The name of the place.
        :type place_name: str
        :return: A dictionary containing information on the place.
        """

        url = cls._BASE_URL + "GetKnownPlace"
        data = {"placeName": place_name}

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_active_alerts(
        cls, alert_types: str = "", alert_causes: str = "", alert_effects: str = ""
    ) -> dict[str, Any]:
        """
        Get active alerts with the given parameters.

        :param alert_types: The types of alerts to get.
        :type alert_types: str
        :param alert_causes: The causes of the alerts to get.
        :type alert_causes: str
        :param alert_effects: The effects of the alerts to get.
        :type alert_effects: str
        :return: A dictionary containing the active alerts.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetActiveAlerts"
        data = {
            "alertTypes": alert_types,
            "alertCauses": alert_causes,
            "alertEffects": alert_effects,
        }

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_alert_causes(cls) -> dict[str, Any]:
        """
        Get the causes of all alerts.

        :return: A dictionary containing the alert causes.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetAlertCauses"

        try:
            response = requests.post(url)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_alert_effects(cls) -> dict[str, Any]:
        """
        Get the effects of all alerts.

        :return: A dictionary containing the alert effects.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetAlertEffects"

        try:
            response = requests.post(url)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_alert_types(cls) -> dict[str, Any]:
        """
        Get the types of all alerts.

        :return: A dictionary containing the alert types.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetAlertTypes"

        try:
            response = requests.post(url)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_all_alerts(cls) -> dict[str, Any]:
        """
        Get all alerts.

        :return: A dictionary containing all alerts.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetAllAlerts"

        try:
            response = requests.post(url)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_all_places(cls) -> dict[str, Any]:
        """
        Get information on all known places.

        :return: A dictionary containing information on all known places.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetAllPlaces"

        try:
            response = requests.post(url)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_arrival_and_departure_times_route(
        cls, route_short_name: str = "", num_of_trips: int = 0, service_date: str = ""
    ) -> dict[str, Any]:
        """
        Get the arrival and departure times for every stop on a given route.

        :param route_short_name: The short name of the route.
        :type route_short_name: str
        :param num_of_trips: The number of trips to return.
        :type num_of_trips: int
        :param service_date: The date of the service.
        :type service_date: str
        :return: The result of the request.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetArrivalAndDepartureTimes"
        data = {
            "routeShortName": route_short_name,
            "numOfTrips": str(num_of_trips),
            "serviceDate": service_date,
        }

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_arrival_and_departure_times_trip(cls, trip_id: int = 0) -> dict[str, Any]:
        """
        Get the arrival and departure times for a given trip.

        :param trip_id: The ID of the trip.
        :type trip_id: int
        :return: The result of the request.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetArrivalAndDepartureTimesTrip"
        data = {"tripID": str(trip_id)}

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_current_bus_info(cls) -> dict[str, Any]:
        """
        Get information on all buses.

        :return: A dictionary containing information on all buses.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetCurrentBusInfo"

        try:
            response = requests.post(url)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_current_routes(cls) -> dict[str, Any]:
        """
        Get information on all routes.

        :return: A dictionary containing information on all routes.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetCurrentRoutes"

        try:
            response = requests.post(url)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_nearest_stops(
        cls, latitude: float = 0.0, longitude: float = 0.0, noOfStops: int = 0
    ) -> dict[str, Any]:
        """
        Get the nearest stops to a given set of GPS coordinates.

        :param latitude: The latitude of the GPS coordinates.
        :type latitude: float
        :param longitude: The longitude of the GPS coordinates.
        :type longitude: float
        :param noOfStops: The number of stops to return.
        :type noOfStops: int
        :return: The result of the request.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetNearestStops"
        data = {
            "latitude": str(latitude),
            "longitude": str(longitude),
            "noOfStops": str(noOfStops),
            "serviceDate": datetime.now().strftime("%m/%d/%y"),
        }

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_next_departures(
        cls, route_short_name: str = "", stop_code: int = 0
    ) -> dict[str, Any]:
        """
        Get the next departures for a given route and stop.

        :param route_short_name: The short name of the route.
        :type route_short_name: str
        :param stop_code: The code of the stop.
        :type stop_code: int
        """

        url = cls._BASE_URL + "GetNextDepartures"
        data = {
            "routeShortName": route_short_name,
            "stopCode": str(stop_code),
            "serviceDate": datetime.now().strftime("%m/%d/%y"),
        }

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_pattern_points_for_pattern_id(
        cls, pattern_id: str = "", service_date: str = ""
    ) -> dict[str, Any]:
        """
        Get information about every stop relative to a given route.

        :param pattern_id: The ID of the pattern.
        :type pattern_id: str
        :param service_date: The date of the service.
        :type service_date: str
        :return: The result of the request.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetPatternPointsForPatternID"
        data = {
            "patternID": pattern_id,
            "serviceDate": service_date,
        }

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_place_types(cls) -> dict[str, Any]:
        """
        Get the types of all known places.

        :return: A dictionary containing the place types.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetPlaceTypes"

        try:
            response = requests.post(url)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_places(cls, place_type: str = "") -> dict[str, Any]:
        """
        Get information on places of a given type.

        :param place_type: The type of place.
        :type place_type: str
        :return: A dictionary containing information on the places.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetPlaces"
        data = {"placeType": place_type}

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_scheduled_pattern_points(cls, pattern_name: str = "") -> dict[str, Any]:
        """
        Get the scheduled pattern points for a given pattern name.

        :param pattern_name: The name of the pattern.
        :type pattern_name: str
        :return: The result of the request.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetScheduledPatternPoints"
        data = {"patternName": pattern_name}

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_scheduled_routes(
        cls, stop_code: int = 0, service_date: str = ""
    ) -> dict[str, Any]:
        """
        Get the scheduled routes for a given stop.

        :param stop_code: The code of the stop.
        :type stop_code: int
        :param service_date: The date of the service.
        :type service_date: str
        :return: The result of the request.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetScheduledRoutes"
        data = {
            "stopCode": str(stop_code),
            "serviceDate": service_date,
        }

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_scheduled_stop_codes(cls, route_short_name: str = "") -> dict[str, Any]:
        """
        Get the scheduled stop codes for a given route.

        :param route_short_name: The short name of the route.
        :type route_short_name: str
        :return: The result of the request.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetScheduledStopCodes"
        data = {"routeShortName": route_short_name}

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_scheduled_stop_info(
        cls, route_short_name: str = "", service_date: str = ""
    ) -> dict[str, Any]:
        """
        Get the scheduled stop information for a given route.

        :param route_short_name: The short name of the route.
        :type route_short_name: str
        :param service_date: The date of the service.
        :type service_date: str
        :return: The result of the request.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetScheduledStopInfo"
        data = {
            "routeShortName": route_short_name,
            "serviceDate": service_date,
        }

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict

    @classmethod
    def get_scheduled_stop_names(cls, route_short_name: str = "") -> dict[str, Any]:
        """
        Get the scheduled stop names for a given route.

        :param route_short_name: The short name of the route.
        :type route_short_name: str
        :return: The result of the request.
        :rtype: dict[str, Any]
        """

        url = cls._BASE_URL + "GetScheduledStopNames"
        data = {"routeShortName": route_short_name}

        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            response_dict = xmltodict.parse(response.text)
        except HTTPException as e:
            raise HTTPException(e)
        return response_dict
