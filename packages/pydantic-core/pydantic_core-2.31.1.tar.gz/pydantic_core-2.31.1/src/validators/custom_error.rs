use pyo3::intern;
use pyo3::prelude::*;
use pyo3::types::PyDict;

use crate::build_tools::py_schema_err;
use crate::errors::ToErrorValue;
use crate::errors::{ErrorType, PydanticCustomError, PydanticKnownError, ValError, ValResult};
use crate::input::Input;
use crate::tools::SchemaDict;

use super::validation_state::ValidationState;
use super::{build_validator, BuildValidator, CombinedValidator, DefinitionsBuilder, Validator};

#[derive(Debug, Clone)]
pub enum CustomError {
    Custom(PydanticCustomError),
    KnownError(PydanticKnownError),
}

impl CustomError {
    pub fn build(
        schema: &Bound<'_, PyDict>,
        _config: Option<&Bound<'_, PyDict>>,
        _definitions: &mut DefinitionsBuilder<CombinedValidator>,
    ) -> PyResult<Option<Self>> {
        let py = schema.py();
        let error_type: String = match schema.get_as(intern!(py, "custom_error_type"))? {
            Some(error_type) => error_type,
            None => return Ok(None),
        };
        let context: Option<Bound<'_, PyDict>> = schema.get_as(intern!(py, "custom_error_context"))?;

        if ErrorType::valid_type(py, &error_type) {
            if schema.contains(intern!(py, "custom_error_message"))? {
                py_schema_err!(
                    "custom_error_message should not be provided if 'custom_error_type' matches a known error"
                )
            } else {
                let error = PydanticKnownError::py_new(py, &error_type, context)?;
                Ok(Some(Self::KnownError(error)))
            }
        } else {
            let error = PydanticCustomError::py_new(
                error_type,
                schema.get_as_req::<String>(intern!(py, "custom_error_message"))?,
                context,
            );
            Ok(Some(Self::Custom(error)))
        }
    }

    pub fn as_val_error(&self, input: impl ToErrorValue) -> ValError {
        match self {
            CustomError::KnownError(ref known_error) => known_error.clone().into_val_error(input),
            CustomError::Custom(ref custom_error) => custom_error.clone().into_val_error(input),
        }
    }
}

#[derive(Debug)]
pub struct CustomErrorValidator {
    validator: Box<CombinedValidator>,
    custom_error: CustomError,
    name: String,
}

impl BuildValidator for CustomErrorValidator {
    const EXPECTED_TYPE: &'static str = "custom-error";

    fn build(
        schema: &Bound<'_, PyDict>,
        config: Option<&Bound<'_, PyDict>>,
        definitions: &mut DefinitionsBuilder<CombinedValidator>,
    ) -> PyResult<CombinedValidator> {
        let custom_error = CustomError::build(schema, config, definitions)?.unwrap();
        let schema = schema.get_as_req(intern!(schema.py(), "schema"))?;
        let validator = Box::new(build_validator(&schema, config, definitions)?);
        let name = format!("{}[{}]", Self::EXPECTED_TYPE, validator.get_name());
        Ok(Self {
            validator,
            custom_error,
            name,
        }
        .into())
    }
}

impl_py_gc_traverse!(CustomErrorValidator { validator });

impl Validator for CustomErrorValidator {
    fn validate<'py>(
        &self,
        py: Python<'py>,
        input: &(impl Input<'py> + ?Sized),
        state: &mut ValidationState<'_, 'py>,
    ) -> ValResult<PyObject> {
        self.validator
            .validate(py, input, state)
            .map_err(|_| self.custom_error.as_val_error(input))
    }

    fn get_name(&self) -> &str {
        &self.name
    }
}
