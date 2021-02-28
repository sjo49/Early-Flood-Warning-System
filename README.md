# CUED Part IA Flood Warning System

This is the Part IA Lent Term computing activity at the Department of
Engineering, University of Cambridge.

The activity is documented at
https://cued-partia-flood-warning.readthedocs.io/. Fork this repository
to start the activity.

RISK LEVEL CRITERIA
Severe risk:
To meet the criteria for severe risk, a town's station must be measuring either: a relative water level greater than ten; or a relative water level greater than eight and have an increasing level over the past two days. If these conditions are met, there is a severe risk of flooding if there is any more rainfall, and so it is appended to the severe risk list.

High risk:
Towns on the high risk list must have a station measuring a relative water level greater than five, and have an arbitrary slope increase higher than -0.5. If there is a significant amount of rainfall, this could become a severe risk town.

Moderate risk:
Towns with stations measuring a relative water level greater than 5, or greater than 2 with an increasing slope, are returned on the moderate risk list. THese towns aren't in any immediate danger, but this could change with consistently bad weather.

Low risk:
The low risk towns have stations measuring a relative water level greater than or equal to 2. There is no apparent danger, however having a relative water level equal to double to typical highest level could eventually lead to problems.