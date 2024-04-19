from phonenumber import geocoder

phone_number = "+919739486161"  # Replace with the phone number you want to look up

country_name = geocoder.description_for_number(phone_number, "en")
print(country_name)