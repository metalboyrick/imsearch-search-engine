import React, { useState, useEffect } from "react"
import firebase from "firebase/app";
import axios from 'axios'
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import "firebase/storage";
import CircularProgress from '@material-ui/core/CircularProgress';
import { InputAdornment } from '@material-ui/core';
import Box from '@material-ui/core/Box';





const firebaseConfig = {
  apiKey: "AIzaSyBmHzDB9jnvzTrOCSLjotOb9fjxc3PqcnQ",
  authDomain: "imsearch-f6bac.firebaseapp.com",
  projectId: "imsearch-f6bac",
  storageBucket: "imsearch-f6bac.appspot.com",
  messagingSenderId: "431383682614",
  appId: "1:431383682614:web:dc98b0bb0f1a46ebf94297"
}

// Initialize Firebase
firebase.initializeApp(firebaseConfig)

// reference to cloud storage
let storage = firebase.storage()

// Create a storage reference from our storage service
var storageRef = storage.ref();

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    overflow: 'hidden',
    backgroundColor: theme.palette.background.paper,
  },
  gridList: {
      position: 'relative',
      float: 'center',
      width: '100%',
      minHeight: '400px',
      minWidth: '664px',
      height: '100% !important'
  },
}));

const App = () => {
  const classes = useStyles();
  const [input, setInput] = useState('')
  const [imgData, setImgData] = useState([])
  const [waiting, setWaiting] = useState(false)
  const [message, setMessage] = useState('')

 
  const onSubmit = (e) => {
    e.preventDefault()
    console.log("searching for: ", input)

    
    setWaiting(true)
    axios({
      method: "GET",
      url: `http://127.0.0.1:8000/search?query=${input}`
    })
      .then(async (res) => {
        
        setImgData([])
        setMessage('')

        let downloadURLs = []
        for (var i = 0; i < 20; i++) {
          try{
            var url = await storageRef.child(`validation/${res.data[i]}`).getDownloadURL()
          } catch (e) {
            continue
          }
          downloadURLs.push(url)
          setImgData(downloadURLs)
        } 

        if (downloadURLs.length == 0){
          setMessage('Picture not found!')
        }
        
        setInput('')
        setWaiting(false)
      })

    
  }

  const tileData = imgData.map(img => ({ 
        img: `${img}`,
        title: 'Image',
        author: 'author',
        cols: 1,
     }))

  
  return(
    <div>
      <TextField
        label="search input"
        margin="normal"
        variant="outlined"
        InputProps={{type: 'search' }}
        onChange={(e) => setInput(e.target.value)}
        InputProps={{endAdornment:  <InputAdornment position='end'>
         <Button variant="contained" color="secondary" onClick={onSubmit}>
          enter
        </Button>
        <Box p={1} bgcolor="background.paper"></Box> 
        {
          waiting == true ? 
          <CircularProgress color="secondary" /> :
          <div />
        }
      </InputAdornment>
       }}
      />

      

      {
        message != '' ?
        <p>{message}</p> :
        <div/>
      }

      <br />
      <div className={classes.root}>
        <GridList className={classes.gridList} cols={5}>
          {tileData.map((tile, index) => (
            <GridListTile key={index} cols={tile.cols || 1}>
              <img src={tile.img} alt={tile.title}/>
            </GridListTile>
          ))}
        </GridList>
      </div>
    </div>
  )
}

export default App;
