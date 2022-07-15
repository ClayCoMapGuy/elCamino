//import logo from './logo.svg';
import './App.css';
import clayconn from './clayconn.svg'

export function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Just some words
        </p>
      </header>
    </div>
  );
}

export function Navbar() {
  return (
    <div className="Navbar">
      <div>
        <a href='https://claytoncountyga.gov'>
          <img src={clayconn} alt='' />
        </a>
      </div>
      <div>
        <p>Clayton County Permitting</p>
      </div>
    </div>
  )
}



//<img src={logo} className="App-logo" alt="logo" />
