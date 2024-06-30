'use client';

import { useState } from "react";
import axios from 'axios';

export default function Home() {
  const [start, setStart] = useState('');
  const [end, setEnd] = useState('');
  const [data, setData] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.get(`http://127.0.0.1:5000/timetable?start=${start}&end=${end}`);
      setData(response.data);
      setError('');
    } catch (err) {
      setError('Error fetching data');
      setData(null);
    }
  };

  return (
    <div>
      <h1>Bus Timetable Finder</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Start Location:
          <input type="text" value={start} onChange={(e) => setStart(e.target.value)} />
        </label>
        <label>
          End Location:
          <input type="text" value={end} onChange={(e) => setEnd(e.target.value)} />
        </label>
        <button type="submit">Find Timetable</button>
      </form>
      {error && <p>{error}</p>}
      {data && (
        <div>
          <h2>Results</h2>
          {data.map((bus, index) => (
            <div key={index}>
              <p>Start: {bus.start}</p>
              <p>End: {bus.end}</p>
              <p>Timetable: {bus.timetable}</p>
              <p>Fare: ${bus.fare}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
