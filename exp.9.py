import numpy as np

# Rewards matrix
R = np.array([
    [-1, -1, -1, -1,  0, -1],
    [-1, -1, -1,  0, -1, 100],
    [-1, -1, -1,  0, -1, -1],
    [-1,  0,  0, -1,  0, -1],
    [ 0, -1, -1,  0, -1, 100],
    [-1,  0, -1, -1,  0, 100]
])

# Initialize Q-table
Q = np.zeros_like(R, dtype=float)

gamma = 0.8
episodes = 1000

# Training
for _ in range(episodes):
    state = np.random.randint(0, 6)

    while state != 5:
        # Find possible actions
        actions = np.where(R[state] >= 0)[0]

        # Select random action
        action = np.random.choice(actions)

        # Move to next state
        next_state = action

        # Update Q-value
        Q[state, action] = (
            R[state, action]
            + gamma * np.max(Q[next_state])
        )

        state = next_state

# Display Q-table
print("Q-Table:\n")
print(Q)
import pandas as pd
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("data.csv")

# Input features
X = data[['Hours_Studied', 'Attendance', 'Assignments']]

# Target variable
y = data['Result']

# Convert labels to numeric values
y = y.map({
    'Fail': 0,
    'Pass': 1
})

# Split dataset into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build Neural Network
model = tf.keras.Sequential([
    tf.keras.Input(shape=(3,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train model
history = model.fit(
    X_train,
    y_train,
    epochs=50,
    validation_split=0.2,
    verbose=1
)

# Predict
y_pred = model.predict(X_test)

# Convert probabilities to class labels
y_pred = (y_pred > 0.5).astype(int).ravel()

# Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
