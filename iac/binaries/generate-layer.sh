source ../../.venv/bin/activate

echo "Updating pip..."
pip install --upgrade pip

if [ ! -f ../../src/requirements.txt ]; then
    echo "requirements.txt. not found in ../../src/requirements.txt"
    deactivate
    exit 1
fi

DEST_DIR="./python/lib/python3.13/site-packages"
echo "making directory: $DEST_DIR"
mkdir -p "$DEST_DIR"

echo "Installing dependencies in requirements.txt on $DEST_DIR..."
pip install -r ../../src/requirements.txt -t "$DEST_DIR" --platform manylinux2014_x86_64 --only-binary=:all: --implementation cp

echo "Deactivating virtual environment..."
deactivate

echo "Creating local modules folder"
UTILS_DIR="$DEST_DIR/src/utils"
mkdir -p "$UTILS_DIR"

echo "Copying the local modules to the output folder"
cp -r ../../src/utils/* "$UTILS_DIR"

echo "compressing layer"
zip -r layers/python3.13-layer.zip python

echo "Deleting python directory"
rm -rf python

echo "!Success! The dependencies have been installed in $DEST_DIR"