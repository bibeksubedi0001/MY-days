a={
    "Name":"Bibek",
    "Percentage":{
        "first terminal":89,
        "second terminal":79,
        "third terminal":98
    },
    "College":"SOS Hermann Gmeiner School"
}
print(a["Percentage"]) 
a["ram"]=43
print(a)
print(a["College"])
print(a.keys())
print(list(a.keys()))
print(a.values())
print(a.items())
print(a.get("College"))
a.update({"ok":"m"})
a["u"]="v"
print(a)


