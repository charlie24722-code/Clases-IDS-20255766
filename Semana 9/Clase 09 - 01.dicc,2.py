birthdays = {
    "Alice": "Apr 1",
    "Bob": "Dec 12",
    "Carol": "Mar 4"
}
birthdays["Carol"] = "Sep 12"
print(birthdays["Carol"])
birthdays["Pau"] = "Jul 31"
print(birthdays)
del birthdays["Bob"]
print(birthdays)

for feliz in birthdays.values():
    print(feliz)

for llaves in birthdays.keys():
    print(llaves)
    
for k, v in birthdays.items():
    print(f"El cumpleaños de {k} es el dia {v}.")