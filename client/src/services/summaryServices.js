import axios from 'axios';

const API_BASE_URL = 'http://localhost:5002'

export const generateSummary = async (data) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/generate`, data);
      return response.data;
    } catch (error) {
      // Handle errors here or throw to be handled where the function is called
      console.error('Error generating summary:', error);
      throw error;
    }
  };
