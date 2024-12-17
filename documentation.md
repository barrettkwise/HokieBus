# Blacksburg Transit Developer API Documentation

## Introduction

The [Blacksburg Transit Developer API](https://ridebt.org/developers) allows developers to access various transit-related data for creating web or mobile applications. Below is a list of all the available methods, including their elements, types, and descriptions.

---

## Endpoints Overview

### 1. CheckForKnownPlace

| **Element**      | **Type**  | **Description**                                   |
|------------------|-----------|---------------------------------------------------|
| `placeName`      | string    | The name of the place to be checked (e.g., "Blacksburg Transit"). |

### 2. GetActiveAlerts

| **Element**      | **Type**  | **Description**                                   |
|------------------|-----------|---------------------------------------------------|
| `alertTypes`     | string    | Gets the types of active alerts.                  |
| `alertCauses`    | string    | Shows the causes of active alerts.                |
| `alertEffects`   | string    | Shows the effects of active alerts.               |

### 3. GetAlertCauses

| **Element**       | **Type**   | **Description**                                 |
|-------------------|------------|-----------------------------------------------|
| `alertCausesID`   | integer    | Specifies ID of alert cause.                  |
| `alertCauseName`  | string     | Specifies the name of the alert cause.        |

### 4. GetAlertEffects

| **Element**       | **Type**   | **Description**                                 |
|-------------------|------------|-----------------------------------------------|
| `alertEffectsID`  | integer    | Specifies ID of alert effect.                  |
| `alertEffectName` | string     | Specifies the name of the alert effect.        |

### 5. GetAlertTypes

| **Element**       | **Type**   | **Description**                                 |
|-------------------|------------|-----------------------------------------------|
| `alertTypesID`    | integer    | Specifies the ID of the alert type.            |
| `alertTypeName`   | string     | Name of the alert type.                        |

### 6. GetAllAlerts

| **Element**       | **Type**   | **Description**                                 |
|-------------------|------------|-----------------------------------------------|
| `alertID`         | integer    | The ID of the alert.                           |
| `alertTypesID`    | integer    | Specifies the ID of the alert type.            |
| `alertCausesID`   | integer    | Specifies the cause ID of the alert.           |
| `alertEffectsID`  | integer    | The ID of the alert effect.                    |
| `alertTitle`      | string     | The title of the alert.                        |
| `alertMessage`    | string     | The message that the alert sends.              |
| `URL`             | string     | URL to view the alert.                         |
| `startDate`       | string     | Start date of alerts (Eastern Standard Time).  |
| `endDate`         | string     | End date of alerts (Eastern Standard Time).    |
| `version`         | dateTime   | Date-time of the latest update.                |
| `alertRank`       | integer    | Degree of alert urgency.                       |

### 7. GetAllPlaces

| **Element**       | **Type**   | **Description**                                 |
|-------------------|------------|-----------------------------------------------|
| `placeID`         | integer    | Specifies the ID of the place.                 |
| `placeTypesID`    | integer    | Specifies the ID of the place type.            |
| `latitude`        | decimal    | Latitude of the place.                         |
| `longitude`       | decimal    | Longitude of the place.                        |
| `placeName`       | string     | Specifies the name of the place.               |
| `display`         | boolean    | Specifies if the place is displayed.           |
| `version`         | dateTime   | Date-time of the latest update.                |

### 8. GetArrivalAndDepartureTimesForRoutes

| **Element**       | **Type**   | **Description**                                 |
|-------------------|------------|-----------------------------------------------|
| `routeShortNames` | string     | The short name of the route (e.g., "HWA" for Hethwood A). |
| `noOfTrips`       | string     | Number of trips for the specified route.       |
| `serviceDate`     | string     | Date of arrival/departure times (Eastern Standard Time). |

### 9. GetCurrentBusInfo

| **Element**          | **Type**    | **Description**                                    |
|----------------------|-------------|--------------------------------------------------|
| `agencyVehicleName`  | string      | Number assigned to the vehicle (e.g., "6403").    |
| `latestEvent`        | string      | Date-time of the latest event for the vehicle.    |
| `latitude`           | decimal     | Latitude.                                        |
| `longitude`          | decimal     | Longitude.                                       |
| `direction`          | integer     | Degree the vehicle is facing at the latestEvent time. |
| `speed`              | string      | Speed of the vehicle at the latestEvent time in MPH. |

### 10. GetNearestStops

| **Element**       | **Type**   | **Description**                                 |
|-------------------|------------|-----------------------------------------------|
| `latitude`        | decimal    | Specify Latitude.                              |
| `longitude`       | decimal    | Specify Longitude.                             |
| `noOfStops`       | string     | Specify the number of closest stops to display. |
| `serviceDate`     | string     | Specify availability by a given service date.  |

---

## General Notes

1. **Date Formats**: Service dates follow the format `YYYY-MM-DD`.
2. **Coordinates**: Latitude and longitude values should be specified in decimal format.
3. **Endpoints**: Access the endpoints through the designated developer API URL provided by Blacksburg Transit.

If you need further information about any of these endpoints or examples of how to use them, please refer to the official API guide provided by **Blacksburg Transit**.
