import React, { useState } from "react"
import axios from 'axios'
import { makeStyles } from '@material-ui/core/styles';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    overflow: 'hidden',
    backgroundColor: theme.palette.background.paper,
  },
  gridList: {
    width: 500,
    height: 450,
  },
}));

const App = () => {
  const classes = useStyles();
  const [input, setInput] = useState('')
  
  const onSubmit = (e) => {
    e.preventDefault()
    console.log(input)

    axios.get(`http://localhost:8000/search?query=${input}`,)
      .then(res => {
        console.log(res);
        console.log(res.data);
      })

    setInput('')
  }

  const tileData = [
    {
      img: 'images/1.jpg',
      title: 'Image',
      author: 'author',
      cols: 2,
    },
    {
      img: 'images/2.jpg',
      title: 'Image',
      author: 'author',
      cols: 1,
    },
    {
      img: 'images/3.jpg',
      title: 'Image',
      author: 'author',
      cols: 3,
    },
    {
      img: 'images/4.jpg',
      title: 'Image',
      author: 'author',
      cols: 1,
    },
    {
      img: 'images/5.jpg',
      title: 'Image',
      author: 'author',
      cols: 2,
    },
  ]
  
  return(
    <div>
      <form onSubmit={onSubmit}>
        <label>
          Search:
          <input type="text" name="name" value={input} onChange={(e) => setInput(e.target.value)}/>
        </label>
        <input type="submit" value="Submit" />
      </form>
      <br />
      <div className={classes.root}>
        <GridList cellHeight={160} className={classes.gridList} cols={3}>
          {tileData.map((tile) => (
            <GridListTile key={tile.img} cols={tile.cols || 1}>
              <img src={tile.img} alt={tile.title} />
            </GridListTile>
          ))}
        </GridList>
      </div>
    </div>
  )
}

export default App;
