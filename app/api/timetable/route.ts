import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const departure = searchParams.get('departure');
  const arrival = searchParams.get('arrival');
  const API_KEY = process.env.NEXT_PUBLIC_BUS_API_KEY;

  const url = `https://data.bus-data.dft.gov.uk/api/v1/dataset/?api_key=${API_KEY}&search=${departure}&limit=5`;

  console.log('Calling API URL:', url);

  try {
    const response = await fetch(url);
    const data = await response.json();
    return NextResponse.json(data);
  } catch (error) {
    console.error('Error fetching timetable data:', error);
    return NextResponse.json({ error: 'Failed to fetch timetable data' }, { status: 500 });
  }
}
