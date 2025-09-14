import os, sys
expected = ['models/knn.joblib', 'models/nb.joblib']
missing = [p for p in expected if not os.path.exists(p)]
if missing:
    print('MISSING FILES:', missing)
    sys.exit(1)
print('All expected model files exist:', expected)
sys.exit(0)
