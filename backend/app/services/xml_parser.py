# app/services/xml_parser.py

import xml.etree.ElementTree as ET
import os

def parse_xml_folder(folder_path):
    routes = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            file_path = os.path.join(folder_path, filename)
            routes.extend(parse_single_xml(file_path))
    return routes

def parse_single_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Define the XML namespace
    ns = {'txc': 'http://www.transxchange.org.uk/'}
    
    routes = []
    
    # Parse StopPoints
    stop_points = {}
    for stop in root.findall('.//txc:AnnotatedStopPointRef', ns):
        stop_ref = stop.find('txc:StopPointRef', ns).text
        stop_name = stop.find('txc:CommonName', ns).text
        stop_points[stop_ref] = stop_name
    
    # Parse JourneyPatternSections
    for jps in root.findall('.//txc:JourneyPatternSection', ns):
        route = []
        for link in jps.findall('txc:JourneyPatternTimingLink', ns):
            from_stop = link.find('txc:From/txc:StopPointRef', ns).text
            to_stop = link.find('txc:To/txc:StopPointRef', ns).text
            if from_stop in stop_points and to_stop in stop_points:
                route.append((stop_points[from_stop], stop_points[to_stop]))
        if route:
            routes.append(route)
    
    return routes

def find_bus_route(routes, start_location, end_location):
    matching_routes = []
    for route in routes:
        start_index = next((i for i, r in enumerate(route) if r[0] == start_location), None)
        if start_index is not None:
            end_index = next((i for i in range(start_index, len(route)) if route[i][1] == end_location), None)
            if end_index is not None:
                matching_routes.append(route[start_index:end_index+1])
    return matching_routes