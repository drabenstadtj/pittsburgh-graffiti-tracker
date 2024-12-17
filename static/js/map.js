// Initialize Leaflet map
const map = L.map("map").setView([40.4406, -79.9959], 12); // Default center: NYC

// Add OpenStreetMap tiles
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "&copy; OpenStreetMap contributors",
}).addTo(map);

// Load existing graffiti markers
function loadGraffiti() {
  fetch("/api/graffiti")
    .then((response) => response.json())
    .then((data) => {
      data.forEach((entry) => {
        L.marker([entry.latitude, entry.longitude])
          .bindPopup(
            `
                        <b>${entry.title}</b><br>
                        ${entry.description}<br>
                        <img src="${entry.image_url}" width="100">
                    `
          )
          .addTo(map);
      });
    })
    .catch((error) => console.error("Error loading graffiti data:", error));
}

// Add a new graffiti entry dynamically
function addGraffiti() {
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;
  const latitude = parseFloat(document.getElementById("latitude").value);
  const longitude = parseFloat(document.getElementById("longitude").value);

  if (!title || !description || isNaN(latitude) || isNaN(longitude)) {
    alert("Please provide valid input for all fields.");
    return;
  }

  // Send POST request to add graffiti
  fetch("/api/graffiti", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: title,
      description: description,
      latitude: latitude,
      longitude: longitude,
      image_url: "static/images/default.png",
      created_by: "User",
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        alert("Graffiti added successfully!");
        L.marker([latitude, longitude])
          .bindPopup(`<b>${title}</b><br>${description}`)
          .addTo(map);
        map.setView([latitude, longitude], 15);
      } else {
        alert("Error: " + data.message);
      }
    })
    .catch((error) => console.error("Error adding graffiti:", error));
}

// Load graffiti markers when the page loads
document.addEventListener("DOMContentLoaded", loadGraffiti);
