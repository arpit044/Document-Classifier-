import axios from "axios";

const API_URL = "http://localhost:8000";

export const processDocument = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  return axios.post(`${API_URL}/process-document/`, formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
};
