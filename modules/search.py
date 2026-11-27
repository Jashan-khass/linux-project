
import psutil


def search_process():

    print("\nPROCESS SEARCH")

    search = input("Enter Process Name or PID: ").strip()

    if not search:
        print("Please enter a process name or PID.")
        return

    found = False

    for process in psutil.process_iter(
        ["pid", "name", "username", "memory_percent"]
    ):

        try:
            info = process.info

            # Search by PID or process name
            if (
                search.lower() in str(info["name"]).lower()
                or search == str(info["pid"])
            ):

                found = True

                print("\nProcess Found!")
                print(f"PID: {info['pid']}")
                print(f"Name: {info['name']}")
                print(f"Username: {info['username']}")
                print(
                    f"RAM Usage: "
                    f"{info['memory_percent']:.2f}%"
                )

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not found:
        print("No matching process found.")


if __name__ == "__main__":
    search_process()


def find_process_data(search_term):
    import psutil

    results = []

    for process in psutil.process_iter(
        attrs=["pid", "name", "username", "memory_percent"]
    ):
        try:
            data = process.info

            pid = str(data["pid"])
            name = data["name"] or ""

            if search_term.lower() in name.lower() or search_term == pid:
                results.append({
                    "pid": data["pid"],
                    "name": name,
                    "username": data["username"],
                    "memory": data["memory_percent"]
                })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return results
