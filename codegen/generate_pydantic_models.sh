# pip install -r requirements-generate.txt
lib_name=aws_sfn_pydantic
script_dir=$(dirname "$(readlink -f "$0")")
repo_dir=$script_dir/asl-validator
if [ ! -d "$source_dir" ]; then
  git clone https://github.com/ChristopheBougere/asl-validator "$repo_dir"
fi
source_dir=$repo_dir/src/schemas
dest_dir=$(readlink -f "$script_dir/../src/$lib_name/generated")
mkdir -p $dest_dir && \
  touch $dest_dir/__init__.py && \
  for input_schema in $source_dir/base-state-machine.json; do
  # for input_schema in $source_dir/*.json; do
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
  done 2> >(tee $script_dir/stderr.log) | tee $script_dir/stdout.log
