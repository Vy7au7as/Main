from pytrends.request import TrendReq


# Get a list of daily trending topics for a specific day
def get_daily_trends_for_day(day):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[""])  # add a dummy keyword
    daily_trends = pytrend.trending_searches(pn="united_states")
    print(f"On the date of {day}\n")
    for i, trend in daily_trends.iterrows():
        print(f"The search term {trend['title']} has {trend['traffic']} amount of traffic")


# Find the interest for a specific keyword
def get_interest_over_time_for_keyword(keyword):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[keyword])
    interest_over_time_df = pytrend.interest_over_time()
    for i, row in interest_over_time_df.iterrows():
        print(f"On the date {i}, the interest value was at {row[keyword]}")


# Command line functionality
option = input("Enter an option (trending or interest): ")
if option == "trending":
    day = input("Enter a date (format: YYYY-MM-DD): ")
    get_daily_trends_for_day(day)
elif option == "interest":
    keyword = input("Enter a keyword: ")
    get_interest_over_time_for_keyword(keyword)
else:
    print("Invalid option")
