"""Run with: python -m unittest discover -s Homework2 -p test_p5_Conrado_Delia.py"""

import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import p5_Conrado_Delia as weather


class WeatherTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.input_path = Path(self.directory.name) / "observations.csv"
        self.output_path = Path(self.directory.name) / "statistics.csv"

    def read_text(self, text):
        self.input_path.write_text(text, encoding="utf-8")
        return weather.read_observations(self.input_path)

    def test_several_stations_negative_temperatures_and_date_sorting(self):
        observations, errors = self.read_text(
            "North,01:00:00 PM 01/01/2026,-10\n"
            "South,09:28:09 AM 04/20/2026,80\n"
            "North,11:00:00 PM 12/31/2025,-20\n"
            "North,09:00:00 AM 01/01/2026,-15\n"
        )
        self.assertEqual(errors, [])
        self.assertEqual(observations, {
            "North": [("11:00:00 PM 12/31/2025", -20.0),
                      ("09:00:00 AM 01/01/2026", -15.0),
                      ("01:00:00 PM 01/01/2026", -10.0)],
            "South": [("09:28:09 AM 04/20/2026", 80.0)],
        })

    def test_duplicate_station_date(self):
        observations, errors = self.read_text(
            "A,09:28:09 AM 04/20/2026,10\n"
            "A,09:28:09 AM 04/20/2026,20\n"
            "B,09:28:09 AM 04/20/2026,30\n"
        )
        self.assertEqual(len(observations["A"]), 1)
        self.assertEqual(observations["A"][0][1], 10.0)
        self.assertIn("B", observations)
        self.assertEqual(errors, [(2, "Duplicate station/date observation")])

    def test_invalid_ranges_and_inclusive_boundaries(self):
        values = ["-100.1", "150.1", "nan", "inf", "-inf", "-100", "150"]
        observations, errors = self.read_text("".join(
            f"S{i},09:28:09 AM 04/20/2026,{value}\n"
            for i, value in enumerate(values)
        ))
        self.assertEqual([number for number, message in errors], [1, 2, 3, 4, 5])
        self.assertEqual(set(observations), {"S5", "S6"})

    def test_malformed_lines_dates_and_nonnumeric_temperatures(self):
        observations, errors = self.read_text(
            "missing fields\n"
            "A,09:28:09 AM 02/30/2026,10\n"
            "A,09:28:09 AM 04/20/2026,warm\n"
            ",09:28:09 AM 04/20/2026,10\n"
            "\n"
            '"unfinished\n'
            "A,09:28:09 AM 04/20/2026,10,extra\n"
            "A,09:28:09 AM 04/20/2026,10\n"
        )
        self.assertEqual([number for number, message in errors], list(range(1, 8)))
        self.assertTrue(all(message for number, message in errors))
        self.assertEqual(observations, {"A": [("09:28:09 AM 04/20/2026", 10.0)]})

    def test_calculated_statistics(self):
        statistics = weather.station_statistics({
            "A": [("date1", -10), ("date2", 5), ("date3", 9)],
            "B": [("date1", 80)],
        })
        self.assertEqual(statistics["A"][:2], (-10, 9))
        self.assertAlmostEqual(statistics["A"][2], 4 / 3)
        self.assertEqual(statistics["B"], (80, 80, 80))

    def test_outliers_use_latest_and_strictly_exceed_mean(self):
        observations, errors = self.read_text(
            "Rising,09:00:00 AM 04/21/2026,20\n"
            "Rising,09:00:00 AM 04/20/2026,10\n"
            "Falling,09:00:00 AM 04/20/2026,20\n"
            "Falling,09:00:00 AM 04/21/2026,10\n"
            "Steady,09:00:00 AM 04/20/2026,15\n"
        )
        self.assertEqual(errors, [])
        self.assertEqual(weather.station_outliers(observations), {
            "Rising": ("09:00:00 AM 04/21/2026", 20.0, 15.0)
        })

    def test_sorted_output_and_one_decimal_place(self):
        weather.write_statistics(self.output_path, {
            "Zulu": (-10, 20, 4 / 3), "Alpha": (1, 2, 1.5)
        })
        self.assertEqual(self.output_path.read_text(encoding="utf-8"),
                         "Alpha,1.0,2.0,1.5\nZulu,-10.0,20.0,1.3\n")

    def test_missing_files(self):
        with self.assertRaises(FileNotFoundError):
            weather.read_observations(self.input_path)
        with self.assertRaises(FileNotFoundError):
            weather.write_statistics(Path(self.directory.name) / "missing" / "out.csv", {})

    def test_empty_input(self):
        self.assertEqual(self.read_text(""), ({}, []))
        self.assertEqual(weather.station_statistics({}), {})
        self.assertEqual(weather.station_outliers({}), {})

    def test_main_success(self):
        self.input_path.write_text("A,09:28:09 AM 04/20/2026,10\n", encoding="utf-8")
        output = io.StringIO()
        with patch.object(weather.sys, "argv", ["weather.py", str(self.input_path), str(self.output_path)]):
            with contextlib.redirect_stdout(output):
                self.assertEqual(weather.main(), 0)
        self.assertIn("A: 10.0, 10.0, 10.0", output.getvalue())
        self.assertIn("Outliers", output.getvalue())
        self.assertEqual(self.output_path.read_text(encoding="utf-8"), "A,10.0,10.0,10.0\n")

    def test_main_handles_file_access_errors(self):
        for operation in ("read_observations", "write_statistics"):
            with self.subTest(operation=operation):
                self.input_path.write_text("", encoding="utf-8")
                error_output = io.StringIO()
                with patch.object(weather.sys, "argv", ["weather.py", str(self.input_path), str(self.output_path)]):
                    with patch.object(weather, operation, side_effect=PermissionError("Access denied")):
                        with contextlib.redirect_stderr(error_output), contextlib.redirect_stdout(io.StringIO()):
                            self.assertEqual(weather.main(), 1)
                self.assertIn("File error:", error_output.getvalue())

    def test_main_missing_input_and_usage(self):
        for arguments in (["weather.py"], ["weather.py", str(self.input_path), str(self.output_path)]):
            with self.subTest(arguments=arguments):
                with patch.object(weather.sys, "argv", arguments):
                    with contextlib.redirect_stderr(io.StringIO()) as output:
                        self.assertEqual(weather.main(), 1)
                self.assertTrue(output.getvalue())


if __name__ == "__main__":
    unittest.main()
