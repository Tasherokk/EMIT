import React from 'react';
import "./page.css";
import CursorFollower from './components/CursorFollower.jsx';
import Link from 'next/link';


function NotFoundPage() {
  return (
    <div className="bg-purple">
       <CursorFollower/>
      <div className="stars">
        <div className="custom-navbar">
          <div className="brand-logo">
            <img src="nas.png" width="80px" alt="Logo" />
          </div>
          <div className="navbar-links">
            <ul>
              <li><a target="_blank">Home</a></li>
              <li><a target="_blank">About</a></li>
              <li><a target="_blank">Creators</a></li>
              <li><a className="btn-request" target="_blank">DONATE</a></li>
            </ul>
          </div>
        </div>
        <div className="central-body">
          <div className="image-404">EMIT</div>
          <Link href="/mapPage">
                <button className="btn-go-home" target="_blank">LAUNCH</button>
          </Link>
        </div>
        <div className="objects">
          <img className="object_rocket" src="http://salehriaz.com/404Page/img/rocket.svg" width="40px" alt="Rocket" />
          <div className="earth-moon">
            <img className="object_earth" src="http://salehriaz.com/404Page/img/earth.svg" width="100px" alt="Earth" />
            <img className="object_moon" src="http://salehriaz.com/404Page/img/moon.svg" width="80px" alt="Moon" />
          </div>
          <div className="box_astronaut">
            <img className="object_astronaut" src="http://salehriaz.com/404Page/img/astronaut.svg" width="140px" alt="Astronaut" />
          </div>
        </div>
        <div className="glowing_stars">
          <div className="star"></div>
          <div className="star"></div>
          <div className="star"></div>
          <div className="star"></div>
          <div className="star"></div>
        </div>
      </div>
    </div>
  );
}

export default NotFoundPage;
