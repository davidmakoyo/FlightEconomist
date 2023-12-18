# FlightEconomist

Python-based application that helps you find flight deals by searching for economical flight prices between a specific origin city and various destination cities. The program uses data from the Sheety API for destination information and the Tequila API for flight searches. You input a list of destinations and price cutoffs into your google sheet and when a flight that meets your criteria within the next six months is found, the program sends you an SMS notification using the Twilio API.

## Introduction

1. **Destination Data Management:** The `data_manager` module fetches destination data from your Sheety API endpoint. You can maintain a Google Sheet that keeps track of the locations you want to visit, along with the price cutoff for each destination. The program reads this data to determine where you wnat to travel and your fare budget for each destination

2. **Flight Search:** The `flight_search` module queries the Tequila API to find flight options between an origin city and various destination cities. It searches for round-trip flights within the next six months.

3. **Flight Deal Alerts:** The program compares the found flight prices with the price cutoffs you've set in the Google Sheet. If a flight fare is lower than the price cutoff, the `notification_manager` module sends an SMS alert to your verified number using the Twilio API.

## Installation

1. Clone the repository:

2. Obtain necessary API keys and credentials:
   - Sheety API: Get the API endpoint from your Sheety account.
   - Tequila API: Get your API key from the Kiwi Tequila API.
   - Twilio API: Obtain your Twilio SID, Auth Token, Virtual Number, and Verified Number.

## Usage

1. Update the API keys and credentials in the appropriate modules as mentioned in the installation steps.

2. Set up and maintain your Google Sheet with destination data and price cutoffs.

3. Run `main.py` to start the flight deal search and notification process.

## Files

- `data_manager.py`: Manages data using the Sheety API for fetching and updating destination information.
- `flight_search.py`: Uses the Tequila API to search for flight deals and retrieve destination codes.
- `flight_data.py`: Defines the `FlightData` class to store flight information.
- `notification_manager.py`: Sends SMS notifications using the Twilio API.
- `main.py`: The main script that orchestrates the entire process.

