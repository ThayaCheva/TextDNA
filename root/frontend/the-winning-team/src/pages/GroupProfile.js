import React from 'react';
import '../css/Group.css'
import Footer from './Footer.js'
import {Link} from 'react-router-dom';

function GroupProfile() {
  const groupData = {
    name: 'COMP30022',
    subjectName: 'IT Project',
    assignments: [
      {
        name: 'Sample Assignment 1',
        status: 80,
        score: 45,
        date: 'Aug 10, 2022',
      },
      {
        name: 'Sample Assignment 1',
        status: 80,
        score: 45,
        date: 'Aug 10, 2022',
      },
      {
        name: 'Sample Assignment 1',
        status: 80,
        score: 45,
        date: 'Aug 10, 2022',
      },
      {
        name: 'Sample Assignment 1',
        status: 80,
        score: 45,
        date: 'Aug 10, 2022',
      },
      {
        name: 'Sample Assignment 1',
        status: 80,
        score: 45,
        date: 'Aug 10, 2022',
      },
      {
        name: 'Sample Assignment 1',
        status: 80,
        score: 45,
        date: 'Aug 10, 2022',
      },
    ],
  };

  return (
    <div>
      <section id="profile">
          <div className="profile-container">
            <div className="profile-info">
              <div className="profile-info-right">
                <h1>{groupData.name}</h1>
                <p>Subject Name: {groupData.subjectName}</p>
                <button className="blue-btn">+ Add Document</button>
              </div>
            </div>
  
            <div className="table">
              <div className="search-container">
                <input type="text" id="search" placeholder="Search Documents"/>
              </div>
              <div className="table-header">
                  <p>Assignment Name</p>
                  <p>Score</p>
                  <p>Submission Date</p>
                  <p>Detail</p>
              </div>
              <div className="table-content">
                {groupData.assignments.map((assignment, index) => (
                  <div className="table-row" key={index}>
                    <div className="file-name">{assignment.name}</div>
                    <div>{assignment.score}%</div>
                    <div>{assignment.date}</div>
                    <div className="row-detail">
                      <img src={require(`../assets/images/download_icon.png`)}></img>
                    <Link to="/assignment">
                      <img src={require(`../assets/images/view_icon.png`)}></img>
                    </Link>
                    </div>
                  </div>
                ))}
              </div>
  
            </div>
  
          </div>
  
          <div className="profile-dashboard">
            <h1>Average Score</h1>
              <img src={require(`../assets/images/graph.png`)}></img>
              <div className="dashboard-info">
                <div className="stats">
                  <h1>6</h1>
                  <p>Total Documents</p>
                </div>
                <div className="stats">
                  <h1>4</h1>
                  <p>High Similarities</p>
                </div>
                <div className="stats">
                  <h1>3</h1>
                  <p>Late Submissions</p>
                </div>
                <div className="stats">
                  <h1>0</h1>
                  <p>Original Texts</p>
                </div>
              </div>
          </div>
        </section>
        <Footer/>
    </div>
  );
}

export default GroupProfile;
