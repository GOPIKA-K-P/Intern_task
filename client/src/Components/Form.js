import React from 'react';

class DownloadCSVButton extends React.Component {
  handleDownloadClick = () => {
    const apiUrl = "http://localhost:8000/download-csv/?api_url=https://www.asterank.com/api/skymorph/search?target=J99TS7A"
    fetch(apiUrl)
      .then((response) => response.blob())
      .then((blob) => {
        const url = window.URL.createObjectURL(new Blob([blob]));
        const a = document.createElement('a');
        a.href = url;
        a.download = 'data.csv';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
      })
      .catch((error) => {
        console.error('Error downloading the CSV:', error);
      });
  }

  render() {
    return (
      <button onClick={this.handleDownloadClick}>Download CSV</button>
    );
  }
}

export default DownloadCSVButton;
