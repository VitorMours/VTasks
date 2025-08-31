function handleImageError(event) {
    const imgElement = event.target;
    imgElement.classList.add('image-failed');
}

module.exports = {
  handleImageError
};
 