# Movie Recommendation System

This project is a Natural Language Processing (NLP) based Movie Recommendation System built using the Bag of Words algorithm. It utilizes a dataset of movies to recommend similar movies based on user input. The user interface is designed using Streamlit, with additional HTML and CSS elements to enhance the appearance. 

## Features

- **Recommendation Engine**: Recommends movies based on the description of the movie entered by the user.
- **Bag of Words Algorithm**: Utilizes the Bag of Words model to process text and recommend similar movies.
- **Interactive UI**: Built using Streamlit for a smooth and interactive user experience.
- **Enhanced Styling**: Custom HTML and CSS for a polished look and feel.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

## Dataset

The dataset used in this project is the TMDb Movie Metadata dataset, available on Kaggle. It contains information about movies including titles, genres, overview, and more.

- [TMDb Movie Metadata Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## API

The project integrates with the TMDb API to fetch additional movie details. You can find more information and get started with the API by visiting the following link:

- [TMDb API Documentation](https://developer.themoviedb.org/docs/getting-started)

## How It Works

1. **Data Preprocessing**: The movie descriptions from the dataset are preprocessed using the Bag of Words technique.
2. **Similarity Calculation**: The similarity between movies is calculated based on the processed text data.
3. **User Input**: The user enters the name or description of a movie.
4. **Recommendation**: The system recommends a list of movies similar to the one entered by the user.

## Usage

1. Enter a movie title or description in the input field.
2. Click the "Recommend" button.
3. View the list of recommended movies based on the entered text.

## Screenshots

![UI Screenshot](screenshot.png)

## Future Enhancements

- **Advanced NLP Techniques**: Implement more sophisticated NLP techniques like TF-IDF or Word2Vec for better recommendations.
- **Collaborative Filtering**: Combine content-based filtering with collaborative filtering for improved recommendations.
- **Improved UI**: Enhance the UI with more detailed movie information and filtering options.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Kaggle](https://www.kaggle.com) for providing the dataset.
- [TMDb](https://www.themoviedb.org/) for the movie API.

---

Feel free to customize this README further to suit your project's needs!
