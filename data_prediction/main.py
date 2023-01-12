import influxdb_client
from datetime import datetime, timedelta
from prediction import ML


def main():
    bucket = "iot"
    org = "univaq"
    token="Fu85EQIX8VDP9447BLHHg3lnJbp0cqkXLK7Ex3-hMrFAXQBjFRN4-u5GDsPQT5vC38ySoulORcJ1qtVpLqJHqQ=="
    url="http://localhost:8086"
    client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

    query_api = client.query_api()
    query = f'from(bucket: "iot") |> range(start: -1d) |> filter(fn: (r) => r["_measurement"] == "SolarPanel0")  |> filter(fn: (r)' \
            f' => r["_field"] == "light" or r["_field"] == "production")  |> yield(name: "mean")'
    query_exec = query_api.query(org=org, query=query)
    lights = query_exec[0].records
    productions = query_exec[1].records

    open("data.csv", "w").close()
    f = open("data.csv", "a")
    f.write("data,target \n")

    data = []
    for index in range(len(lights)):
        data.append((lights[index].get_value(), productions[index].get_value()))
        light = int(lights[index].get_value())
        production = int(productions[index].get_value())
        f.write(f"{light}, {production} \n")

    f.close()



if __name__ == '__main__':
    ml = ML()
    print(ml.predict(0))