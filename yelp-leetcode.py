def timePercentage(query, business):
    query_start = float(query.split('-')[0])
    query_end = float(query.split('-')[1])

    if query_start == query_end:
        return None

    business_start = float(business.split('-')[0])
    business_end = float(business.split('-')[1])

    intersection_start = max(query_start, business_start)
    intersection_end = min(query_end, business_end)

    return (intersection_end-intersection_start)/(query_end-query_start)