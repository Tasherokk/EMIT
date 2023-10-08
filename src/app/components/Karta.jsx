'use client'

import React from "react";
import { GoogleMap, useJsApiLoader } from "@react-google-maps/api";
import "./karta.css"; // Импортируйте стили из вашего CSS-файла

const containerStyle = {
  width: "100%", // картан
  height: "100vh",
};

const center = {
  lat: 43.222,
  lng: 76.8512,
};

// рендироваем для и сайт делаем визуал сайьы
function Karta() {
  //Вы используете хук useJsApiLoader для загрузки Google Maps JavaScript API и проверки, была ли загрузка успешной:

  // Деструктуризация объекта: const { isLoaded } = useJsApiLoader(...)
  // isLoaded - это переменная, в которой будет содержаться булевое значение (true или false), указывающее, была ли успешно загружена библиотека Google Maps API.

  const { isLoaded } = useJsApiLoader({
    id: "google-map-script",
    googleMapsApiKey: "AIzaSyCVJ2v5vloOnxSq4tCHgZvs3i0I8ILKgJQ",
  });

  const [map, setMap] = React.useState(null); // он мотрит есит ли вообще карта

  //

  const onLoad = React.useCallback(function callback(map) {
    const bounds = new window.google.maps.LatLngBounds(center);
    map.fitBounds(bounds);

    setMap(map);
  }, []); //

  const onUnmount = React.useCallback(function callback(map) {
    setMap(null);
  }, []); //

  return (
    <div className="main">
      <div className="map-container">
        {" "}
        {/* Применяем стили через CSS */}
        {isLoaded ? (
          <GoogleMap
            mapContainerStyle={containerStyle}
            center={center}
            zoom={1}
            onLoad={onLoad}
            onUnmount={onUnmount}
          >
            {/* Дочерние компоненты, такие как маркеры, информационные окна, и так далее */}
            <></>
          </GoogleMap>
        ) : (
          <></>
        )}
      </div>
      <div className="button-container">
        <div className="menu-button">
          <div className="line"></div>
          <div className="line"></div>
          <div className="line"></div>
        </div>
      </div>
    </div>
  );
}

export default React.memo(Karta);

{
  /* <div class="main">
    <div class="button-container">
        <button class="button">EMIT</button>
    </div>
    <div class="map-container">
        <!-- здесь интеграция с Google Maps -->
    </div>
</div> */
}