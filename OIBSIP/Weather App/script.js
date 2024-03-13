function getWeather() {
    const apiKey = '3b67eaa48178822058fcfd7eea6a213d'; // Replace with your actual API key
    const city = document.getElementById('cityInput').value;
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;
  
    fetch(url)
      .then(response => response.json())
      .then(data => {
        const weatherInfo = document.getElementById('weatherInfo');
        if (data.cod === '404') {
          weatherInfo.innerHTML = `<p>${data.message}</p>`;
        } else {
          const weatherDescription = data.weather[0].description;
          const temperature = data.main.temp;
          const humidity = data.main.humidity;
          const windSpeed = data.wind.speed;
          weatherInfo.innerHTML = `
            <p>Weather: ${weatherDescription}</p>
            <p>Temperature: ${temperature}°C</p>
            <p>Humidity: ${humidity}%</p>
            <p>Wind Speed: ${windSpeed} m/s</p>
          `;
        }
      })
      .catch(error => {
        console.error('Error fetching weather data:', error);
      });
  }
  