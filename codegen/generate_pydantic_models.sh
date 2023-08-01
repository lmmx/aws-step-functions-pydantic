# pip install -r requirements-generate.txt
script_dir=$(dirname "$(readlink -f "$0")")
repo_dir=$script_dir/asl-validator
source_dir=$repo_dir/src/schemas
if [ ! -d "$source_dir" ]; then
  git clone https://github.com/ChristopheBougere/asl-validator "$repo_dir"
else
dest_dir=$(readlink -f "$script_dir/../src/aws_step_functions_pydantic/generated")
touch $source_dir && \
  mkdir -p $dest_dir && \
  touch $dest_dir/__init__.py && \
  for input_schema in $source_dir/*.json; do
    output_file=$dest_dir/$(basename ${input_schema%.*} | tr '-' '_').py
    echo "BEGINNING processing $input_schema --> $output_file"
    datamodel-codegen \
      --input $input_schema \
      --input-file-type jsonschema \
      --output $output_file \
      --output-model-type pydantic_v2.BaseModel \
      --target-python-version 3.10 \
      --enum-field-as-literal one \
      --strict-nullable
    echo
    echo "FINISHED processing $input_schema"
    echo
  done 2> >(tee stderr.log) | tee stdout.log
