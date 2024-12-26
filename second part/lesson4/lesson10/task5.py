def analyze_ad_efficiency(clicks, impressions, views):
    if impressions == 0:
        return "Uncertain"
    
    click_to_impression_ratio = clicks / impressions

    if click_to_impression_ratio < 0.01 and views > impressions:
        return "Underestimated"
    elif 0.01 <= click_to_impression_ratio < 0.05:
        return "Low"
    elif 0.05 <= click_to_impression_ratio < 0.1 and views > clicks:
        return "Average"
    elif click_to_impression_ratio >= 0.1:
        return "High"
    else:
        return "Uncertain"
    
print(analyze_ad_efficiency(50, 10000, 15000))
print(analyze_ad_efficiency(200, 10000, 5000))
print(analyze_ad_efficiency(700, 10000, 800))
print(analyze_ad_efficiency(1200, 10000, 1000))
print(analyze_ad_efficiency(500, 10000, 200))