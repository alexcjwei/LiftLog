// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { initializeAuth, connectAuthEmulator } from 'firebase/auth';
//@ts-ignore
import { getReactNativePersistence } from '@firebase/auth/dist/rn/index.js';
import AsyncStorage from '@react-native-async-storage/async-storage';

const firebaseConfig = {
  apiKey: 'AIzaSyCHQJdDdFTG7607DJL7vqlvQd9ZzU8SeUE',
  authDomain: 'liftlog-1a6cd.firebaseapp.com',
  projectId: 'liftlog-1a6cd',
  storageBucket: 'liftlog-1a6cd.appspot.com',
  messagingSenderId: '688805042506',
  appId: '1:688805042506:web:f4b057ca78109fecef89b3',
  measurementId: 'G-K2PYSFLPD7',
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const auth = initializeAuth(app, {
  persistence: getReactNativePersistence(AsyncStorage),
});
connectAuthEmulator(auth, 'http://localhost:9099');
