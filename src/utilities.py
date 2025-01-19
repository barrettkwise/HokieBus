import json
import xml.etree.ElementTree as ET
from typing import Any

import requests


def __req_get_nearest_stops(
    latitude: float, longitude: float, noOfStops: int, serviceDate: str
) -> dict[str, Any]:
    """
    Get the nearest stops to a given set of GPS coordinates.

    :param latitude: The latitude of the GPS coordinates.
    :type latitude: float
    :param longitude: The longitude of the GPS coordinates.
    :type longitude: float
    :param noOfStops: The number of stops to return.
    :type noOfStops: int
    :param serviceDate: The service date.
    :type serviceDate: str
    :return: The result of the request.
    :rtype: dict[str, Any]
    """

    url = "http://216.252.195.248/webservices/bt4u_webservice.asmx/GetNearestStops"
    data = {
        "latitude": str(latitude),
        "longitude": str(longitude),
        "noOfStops": str(noOfStops),
        "serviceDate": serviceDate,
    }

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an exception for HTTP errors

        root = ET.fromstring(response.content)
        result = [
            {
                "StopName": stop.find("StopName").text,
                "StopCode": stop.find("StopCode").text,
                "Feet": float(stop.find("Feet").text),
                "Miles": float(stop.find("Miles").text),
                "Latitude": float(stop.find("Latitude").text),
                "Longitude": float(stop.find("Longitude").text),
            }
            for stop in root.findall("StopDistances")
        ]
        exception = None
    except requests.exceptions.RequestException as e:
        response = None
        root = None
        result = []
        exception = e

    return {
        "given_cords": (latitude, longitude),
        "status_code": response.status_code if response else None,
        "content": response.content if response else None,
        "json": json.dumps(result, indent=2),
        "xml": root,
        "exception": exception,
    }


def __req_get_arrival_and_departure_times_for_trip(tripID: str) -> dict[str, Any]:
    try:
        req = requests.post(
            "http://216.252.195.248/webservices/bt4u_webservice.asmx/GetArrivalAndDepartureTimesForTrip",
            data={"tripID": tripID},
        )
        content = req.content
        code = req.status_code
        root = ET.fromstring(content)
        exception = None
    except requests.exceptions.RequestException as e:
        content = None
        code = None
        root = None
        exception = e

    return {
        "status_code": code,
        "content": content,
        "xml": root,
        "exception": exception,
    }

def __req_get_current_bus_info() -> dict[str, Any]:
    try:
        req = requests.post(
            "http://216.252.195.248/webservices/bt4u_webservice.asmx/GetCurrentBusInfo",
        )
        content = req.content
        code = req.status_code
        root = ET.fromstring(content)
        exception = None
    except requests.exceptions.RequestException as e:
        content = None
        code = None
        root = None
        exception = e

    return {
        "status_code": code,
        "content": content,
        "xml": root,
        "exception": exception,
    }


def __req_get_current_routes() -> dict[str, Any]:
    exception = None
    try:
        req = requests.post(
            "http://216.252.195.248/webservices/bt4u_webservice.asmx/GetCurrentRoutes"
        )
    except requests.exceptions.RequestException as e:
        exception = e

    if not exception:
        content = req.content
        code = req.status_code
        root = ET.fromstring(req.content)
    else:
        code = None
        root = None
        content = None

    return {
        "status_code": code,
        "content": content,
        "xml": root,
        "exception": exception,
    }


def __req_get_next_departures(routeShortName: str, stopCode: int) -> dict[str, Any]:
    exception = None
    try:
        req = requests.post(
            "http://216.252.195.248/webservices/bt4u_webservice.asmx/GetNextDepartures",
            data={"routeShortName": routeShortName, "stopCode": stopCode},
        )
    except requests.exceptions.RequestException as e:
        exception = e

    if not exception:
        content = req.content
        code = req.status_code
        root = ET.fromstring(req.content)
    else:
        code = None
        root = None
        content = None

    return {
        "status_code": code,
        "content": content,
        "xml": root,
        "exception": exception,
    }


def __req_get_scheduled_pattern_points(patternName: str) -> dict[str, Any]:
    exception = None
    try:
        req = requests.post(
            "http://216.252.195.248/webservices/bt4u_webservice.asmx/GetScheduledPatternPoints",
            data={"patternName": patternName},
        )
    except requests.exceptions.RequestException as e:
        exception = e

    if not exception:
        content = req.content
        code = req.status_code
        root = ET.fromstring(req.content)
    else:
        code = None
        root = None
        content = None

    return {
        "status_code": code,
        "content": content,
        "xml": root,
        "exception": exception,
    }


def __req_get_scheduled_routes(stopCode: int) -> dict[str, Any]:
    exception = None
    try:
        req = requests.post(
            "http://216.252.195.248/webservices/bt4u_webservice.asmx/GetScheduledRoutes",
            data={"stopCode": stopCode},
        )
    except requests.exceptions.RequestException as e:
        exception = e

    if not exception:
        content = req.content
        code = req.status_code
        root = ET.fromstring(req.content)
    else:
        code = None
        root = None
        content = None

    return {
        "status_code": code,
        "content": content,
        "xml": root,
        "exception": exception,
    }


def __req_get_scheduled_stop_codes(routeShortName: str) -> dict[str, Any]:
    exception = None
    try:
        req = requests.post(
            "http://216.252.195.248/webservices/bt4u_webservice.asmx/GetScheduledStopCodes",
            data={"routeShortName": routeShortName},
        )
    except requests.exceptions.RequestException as e:
        exception = e

    if not exception:
        content = req.content
        code = req.status_code
        root = ET.fromstring(req.content)
    else:
        code = None
        root = None
        content = None

    return {
        "status_code": code,
        "content": content,
        "xml": root,
        "exception": exception,
    }


def __req_get_scheduled_stop_names(routeShortName: str) -> dict[str, Any]:
    exception = None
    try:
        req = requests.post(
            "http://216.252.195.248/webservices/bt4u_webservice.asmx/GetScheduledStopNames",
            data={"routeShortName": routeShortName},
        )
    except requests.exceptions.RequestException as e:
        exception = e

    if not exception:
        content = req.content
        code = req.status_code
        root = ET.fromstring(req.content)
    else:
        code = None
        root = None
        content = None

    return {
        "status_code": code,
        "content": content,
        "xml": root,
        "exception": exception,
    }


def __req_get_summary(stopCode: int) -> dict[str, Any]:
    exception = None
    try:
        req = requests.post(
            "http://216.252.195.248/webservices/bt4u_webservice.asmx/GetSummary"
        )
    except requests.exceptions.RequestException as e:
        exception = e

    if not exception:
        content = req.content
        code = req.status_code
        root = ET.fromstring(req.content)
    else:
        code = None
        root = None
        content = None

    return {
        "status_code": code,
        "content": content,
        "xml": root,
        "exception": exception,
    }


def is_current_route(routeShortName: str) -> bool:
    resp = __req_get_current_routes()
    currentRoutes = []
    if resp["status_code"] is not None and resp["status_code"] == 200:
        for child in resp["xml"].iter("CurrentRoutes"):
            currentRoutes.append(child.find("RouteShortName").text.lower())
    return routeShortName in currentRoutes


def get_next_departure_times_for_route_and_stop_code(
    routeShortName: str, stopCode: int, numTimesToReturn=5
) -> dict[str, Any]:
    results = []

    resp = __req_get_next_departures(routeShortName, stopCode)
    success = True
    error = None
    if resp["status_code"] is not None and resp["status_code"] == 200:
        for child in resp["xml"].iter("AdjustedDepartureTime"):
            results.append(child.text)
        sorted(results)
        if len(results) == 0:
            success = False
            error = "<Message>It looks like there are no buses currently running for that route and stop. You could try just sending the stop number to see all current routes at this location.</Message>"
    else:
        success = False

    return {
        "success": success,
        "status_code": resp["status_code"],
        "times": results[:numTimesToReturn],
        "error": error,
    }


def get_buses_for_stop_code(stopCode: int) -> dict[str, Any]:
    resp = __req_get_scheduled_routes(stopCode)

    success = True
    route_short_names = []
    route_names = []
    routes = {}

    if len(resp["xml"].findall(".//Error")) > 0:
        # Successful response from server, but likely a bad stop number. We'll see if there are any routes in the calling function to handle
        success = False

    else:
        # pudb.set_trace()

        if resp["status_code"] is not None and resp["status_code"] == 200:
            for child in resp["xml"].iter("RouteShortName"):
                route_short_names.append(child.text)
            for child in resp["xml"].iter("RouteName"):
                route_names.append(child.text)
            for child in resp["xml"].iter("ScheduledRoutes"):
                routes[child.find("RouteShortName").text] = child.find("RouteName").text
        else:
            success = False

        if len(routes) == 0:
            # Bad stop number likely
            success = False

    return {
        "success": success,
        "status_code": resp["status_code"],
        "route_short_names": route_short_names,
        "route_names": route_names,
        "routes": routes,
    }


def get_times_for_stop_code(stopCode: int, requestShortNames: bool) -> dict[str, Any]:
    buses_resp = get_buses_for_stop_code(stopCode)

    times = []
    success = buses_resp["success"]
    if (
        buses_resp["status_code"] is not None
        and buses_resp["status_code"] == 200
        and success
    ):
        buses = buses_resp["route_short_names"]

        numTimesToReturn = 1

        if len(buses) == 0:
            return {"success": True, "times": None}

        if len(buses) <= 2:
            numTimesToReturn = 3

        for route in buses:
            next_deps = get_next_departure_times_for_route_and_stop_code(
                route, stopCode, numTimesToReturn
            )

            if next_deps["status_code"] != None and next_deps["status_code"] == 200:
                if requestShortNames == True:
                    times.append((route, next_deps["times"]))
                else:
                    times.append((buses_resp["routes"][route], next_deps["times"]))
            else:
                success = False
                break
    elif (
        buses_resp["status_code"] is not None
        and buses_resp["status_code"] == 200
        and not success
        and len(buses_resp["routes"]) == 0
    ):
        # No routes were listed, so probably an invalid stop number
        success = "Invalid"
    else:
        success = False

    return {"success": success, "times": times}
