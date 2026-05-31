def auto_category(text):
    
    text = text.lower()

    if "zomato" in text:
        return "Food"

    if "swiggy" in text:
        return "Food"

    if "uber" in text:
        return "Travel"

    if "ola" in text:
        return "Travel"

    if "amazon" in text:
        return "Shopping"

    if "flipkart" in text:
        return "Shopping"

    if "rent" in text:
        return "Rent"

    return "Other"