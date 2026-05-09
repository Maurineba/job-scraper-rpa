def parse_salary(value):
   if not value:
      return 0

   value = value.lower()

   if "a combinar" in value:
      return 0

   value = value.replace("r$", "")
   value = value.replace(".", "")
   value = value.replace(",", ".")
   value = value.strip()

   try:
      return float(value)
   except:
      return 0
