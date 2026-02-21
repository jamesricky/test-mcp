import httpx

SPACEX_API_BASE = "https://api.spacexdata.com/v4"


async def launches(launch_year: int | None = None) -> str:
    """Get SpaceX launches. Optionally filter by year.

    Args:
        launch_year: Optional year to filter launches (e.g. 2020).
                     If not provided, returns all launches.
    """
    async with httpx.AsyncClient() as client:
        if launch_year is not None:
            response = await client.post(
                f"{SPACEX_API_BASE}/launches/query",
                json={
                    "query": {
                        "date_utc": {
                            "$gte": f"{launch_year}-01-01T00:00:00.000Z",
                            "$lte": f"{launch_year}-12-31T23:59:59.999Z",
                        }
                    },
                    "options": {"sort": {"date_utc": "asc"}},
                },
                timeout=30.0,
            )
        else:
            response = await client.get(
                f"{SPACEX_API_BASE}/launches",
                timeout=30.0,
            )

        response.raise_for_status()
        data = response.json()

        # Query endpoint wraps results in {"docs": [...]}
        launch_list = data.get("docs", data) if isinstance(data, dict) else data

        if not launch_list:
            return "No launches found."

        results = []
        for launch in launch_list:
            result = (
                f"Flight #{launch.get('flight_number')} - {launch.get('name')}\n"
                f"  Date: {launch.get('date_utc', 'Unknown')}\n"
                f"  Success: {launch.get('success', 'Unknown')}\n"
                f"  Details: {launch.get('details') or 'No details available'}"
            )
            results.append(result)

        header = (
            f"SpaceX Launches ({launch_year})"
            if launch_year
            else "All SpaceX Launches"
        )
        return f"{header} - {len(results)} launches found\n\n" + "\n\n".join(results)
