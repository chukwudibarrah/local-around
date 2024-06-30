'use client';

import { useState } from "react";

interface TimetableData {
  count?: number;
  next?: string | null;
  previous?: string | null;
  results: any[];
}

interface TimetableError {
  error: string;
}

type TimetableResponse = TimetableData | TimetableError | null;

export default function Home() {
  const [departureStation, setDepartureStation] = useState("");
  const [arrivalStation, setArrivalStation] = useState("");
  const [timetableData, setTimetableData] = useState<TimetableResponse>(null);

  const fetchTimetableData = async () => {
    try {
      const response = await fetch(`/api/timetable?departure=${departureStation}&arrival=${arrivalStation}`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data: TimetableData = await response.json();
      console.log('API response:', data);
      setTimetableData(data);
    } catch (error) {
      console.error("Error fetching timetable data:", error);
      setTimetableData({ error: 'Failed to fetch data' });
    }
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    fetchTimetableData();
  };

  return (
    <main className="w-screen h-screen flex flex-col justify-center items-center">
      <div className="space-y-16 flex flex-col items-center">
        <div>
          <h1>Plan your journey</h1>
        </div>
        <div>
          <form onSubmit={handleSubmit} className="space-y-10">
            <div>
              <input
                type="text"
                placeholder="Departing from"
                className="p-5 bg-transparent border-2 border-gray-300"
                value={departureStation}
                onChange={(e) => setDepartureStation(e.target.value)}
              />
              <input
                type="text"
                placeholder="Going to"
                className="p-5 bg-transparent border-2 border-gray-300"
                value={arrivalStation}
                onChange={(e) => setArrivalStation(e.target.value)}
              />
            </div>
            <div>
              <button type="submit">Get times and prices</button>
            </div>
          </form>
        </div>
        {timetableData && (
          <div>
            <h2>Timetable Results:</h2>
            <pre>{JSON.stringify(timetableData, null, 2)}</pre>
          </div>
        )}
      </div>
    </main>
  );
}
