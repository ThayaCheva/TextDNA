import React from 'react';
import '../css/pages/Landing.css'
import Footer from './Footer'

function Landing() {
  return (
    <div>
      <section id="landing">
        <div className="landing-main">
          <div className="landing-main-left"> 
            <h1 className = "main-header"> A <span className="bold-word">Streamlined</span> Process to Authorship Attribution </h1>
            <p className = "main-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
            <button className="get-started-button">GET STARTED</button>
          </div>
          <div className="landing-main-right">
                <img src={require(`../assets/images/landing-main.png`)} className='main-image'></img>
          </div>
            
        </div>

        <div className="image-container">
          <img src={require(`../assets/images/right-banner.png`)} alt="right-banner" className='right-banner'/>
          <img src={require(`../assets/images/left-banner.png`)} alt="left-banner" className='left-banner'/>
          <div className="image-box">
            <img src={require(`../assets/images/used-by.png`)} alt="Image-1" className="image"/>
            <p className="image-text"><span className="banner-bold-white">Used by</span> <span className="banner-bold-black">100+ </span> 
            <span className="banner-bold-white">institutes</span></p>
          </div>
          <div className="image-box">
            <img src={require(`../assets/images/registered.png`)} alt="Image 2" className="image"/>
            <p className="image-text"><span className="banner-bold-black">2000+ </span> 
            <span className="banner-bold-white">registered profiles</span></p>
          </div>
          <div className="image-box">
            <img src={require(`../assets/images/attributions.png`)} alt="Image 3" className="image"/>
            <p className="image-text"><span className="banner-bold-white">Get</span> <span className="banner-bold-black">fast</span> <span className="banner-bold-white">and</span> 
            <span className="banner-bold-black"> reliable</span> <span className="banner-bold-white">attribution</span></p>
          </div>
        </div>

        <div className = "instructions">
          <div className = "instruction-left1"> 
            <img src={require(`../assets/images/landing1.png`)} alt="instruction-image"></img>
          </div>
  
          <div className = "text">
          <h1 className = "text-header"><span className="bold-word">Create</span> your profile!</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
          </div>
        </div>
        
        <div className = "instructions">
            <div className = "text">
            <h1 className = "text-header"><span className="bold-word">Upload</span> student profiles!</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
          </div>
          
          <div className = "instruction-right"> 
            <img src={require(`../assets/images/landing2.png`)} alt="instruction-image"></img>
          </div>
        </div>

        <div className = "instructions">
          <div className = "instruction-left"> 
            <img src={require(`../assets/images/landing3.png`)} id="instruction-image"></img>
          </div>
  
          <div className = "text">
          <h1 className = "text-header"><span className="bold-word">Get</span> a score back!</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. </p>
          </div>
        </div>
        
      </section>
      <Footer/>
    </div>
  );
}

export default Landing;
