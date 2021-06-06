import React, { useState, useEffect } from "react"
import axios from 'axios'
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';



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
  
  const onSubmit = (e) => {
    e.preventDefault()
    console.log("searching for: ", input)

    axios.get(`http://localhost:8000/search?query=${input}`,)
      .then(res => {
        console.log(res);
        console.log(res.data);
        setImgData(res.data)
      })

    setInput('')
  }

  const tileData = imgData.map(img => ({ 
        img: `images/${img}`,
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
        InputProps={{endAdornment: <Button variant="contained" color="secondary" onClick={onSubmit}>
        enter
      </Button>}}
      />

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
