import '../App.css';
import clayconn from '../Graphics/clayconn.svg';

export default function Navbar() {
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
