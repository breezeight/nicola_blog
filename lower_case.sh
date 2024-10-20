for FILE in *; do
  LOWERCASE=$(echo "$FILE" | tr '[:upper:]' '[:lower:]')
  if [ "$FILE" != "$LOWERCASE" ]; then
    git mv "$FILE" "$LOWERCASE"
  fi
done

