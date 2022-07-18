import '../App.css';
import clayconn from '../Graphics/clayconn.svg';

export  function Navbar() {
  return (
    <div className="Navbar">
      <div>
        <a href='https://claytoncountyga.gov'>
          <img src={clayconn} alt='County Logo' />
        </a>
      </div>
      <ul className="menuItems">
      <li><a href="#">Clayton County Permitting</a></li>
      <li><a href="claytoncountyga.gov/">Go to Claytoncountyga.gov</a></li>
      <li></li>
      <li></li>
      </ul>
        
      
    </div>
  )
}
