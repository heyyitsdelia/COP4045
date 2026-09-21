"""Analyze station temperatures. Usage: python p5_Conrado_Delia.py input.csv output.csv."""

import csv
import datetime
import sys


DATE_FORMAT = "%I:%M:%S %p %m/%d/%Y"


def read_observations(filename):
    """Return station observations and (line number, message) errors.

    Dates remain strings, but datetime is used for validation and chronological
    sorting. The input has no header. File access errors propagate to the caller.
    """
    observations = {}
    errors = []
    seen = set()

    with open(filename, "r", encoding="utf-8", newline="") as input_file:
        for line_number, line in enumerate(input_file, start=1):
            try:
                fields = next(csv.reader([line], strict=True))
            except csv.Error:
                errors.append((line_number, "Malformed CSV line"))
                continue

            if len(fields) != 3:
                errors.append((line_number, "Expected station,date,temperature"))
                continue

            station, date, temperature_text = [field.strip() for field in fields]
            if not station:
                errors.append((line_number, "Station must not be empty"))
                continue

            try:
                timestamp = datetime.datetime.strptime(date, DATE_FORMAT)
            except ValueError:
                errors.append((line_number, "Invalid date; expected HH:MM:SS AM/PM MM/DD/YYYY"))
                continue

            try:
                temperature = float(temperature_text)
            except ValueError:
                errors.append((line_number, "Temperature must be a number"))
                continue

            # This comparison also rejects NaN and positive/negative infinity.
            if not -100.0 <= temperature <= 150.0:
                errors.append((line_number, "Temperature must be between -100.0 and 150.0"))
                continue

            key = (station, timestamp)
            if key in seen:
                errors.append((line_number, "Duplicate station/date observation"))
                continue

            seen.add(key)
            observations.setdefault(station, []).append((date, temperature))

    for readings in observations.values():
        readings.sort(key=lambda reading: datetime.datetime.strptime(reading[0], DATE_FORMAT))

    return observations, errors


def station_statistics(observations):
    """Return {station: (minimum, maximum, mean)} for nonempty stations."""
    statistics = {}
    for station, readings in observations.items():
        if readings:
            temperatures = [temperature for date, temperature in readings]
            statistics[station] = (
                min(temperatures),
                max(temperatures),
                sum(temperatures) / len(temperatures),
            )
    return statistics


def station_outliers(observations):
    """Return latest readings above the station mean; input is sorted by date."""
    statistics = station_statistics(observations)
    return {
        station: (readings[-1][0], readings[-1][1], statistics[station][2])
        for station, readings in observations.items()
        if readings and readings[-1][1] > statistics[station][2]
    }


def write_statistics(filename, statistics):
    """Write headerless station,min,max,mean CSV rows in lexicographic order.

    Statistics contain one row per station; individual dated observations are
    not part of this function's input. All temperatures have one decimal place.
    """
    with open(filename, "w", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file)
        for station in sorted(statistics):
            minimum, maximum, mean = statistics[station]
            writer.writerow([station, f"{minimum:.1f}", f"{maximum:.1f}", f"{mean:.1f}"])


def main():
    """Read command-line filenames, report results, and gracefully handle I/O errors."""
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} input.csv output.csv", file=sys.stderr)
        return 1

    try:
        observations, errors = read_observations(sys.argv[1])
        for line_number, message in errors:
            print(f"Line {line_number}: {message}", file=sys.stderr)

        statistics = station_statistics(observations)
        outliers = station_outliers(observations)

        print("Statistics (station, minimum, maximum, mean):")
        for station in sorted(statistics):
            minimum, maximum, mean = statistics[station]
            print(f"{station}: {minimum:.1f}, {maximum:.1f}, {mean:.1f}")

        print("Outliers (station, date, temperature, mean):")
        for station in sorted(outliers):
            date, temperature, mean = outliers[station]
            print(f"{station}: {date}, {temperature:.1f}, {mean:.1f}")

        write_statistics(sys.argv[2], statistics)
    except (OSError, UnicodeError) as error:
        print(f"File error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
