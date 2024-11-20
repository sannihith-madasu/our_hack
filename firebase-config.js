import { initializeApp } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-app.js";
import { getAuth, 
         GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-firestore.js";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDU8bt82WxGldYYS3rMHYgEz2h0i4rdtT0",
  authDomain: "destin8-fb470.firebaseapp.com",
  projectId: "destin8-fb470",
  storageBucket: "destin8-fb470.firebasestorage.app",
  messagingSenderId: "214648814685",
  appId: "1:214648814685:web:957649cbf77018657aa1b4",
  measurementId: "G-BQF6679GS6"
};

  // Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

const db = getFirestore(app);

export { auth, provider, db };