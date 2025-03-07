use pyo3::class::basic::CompareOp;
use pyo3::prelude::*;
use pyo3::types::PyDict;
use pyo3::types::PyIterator;
use pyo3::types::PyList;
use pyo3::types::PySet;
use pyo3::types::PyTuple;
use pyo3::types::PyType;

#[pyclass]
struct PinqSeq {
    items: Vec<PyObject>,
    pointer: usize,
}

#[pymethods]
impl PinqSeq {
    #[new]
    fn new(items: &Bound<'_, PyList>) -> PyResult<Self> {
        let mut vec_items = Vec::with_capacity(items.len());
        for item in items.iter() {
            vec_items.push(item.into());
        }
        Ok(PinqSeq {
            items: vec_items,
            pointer: 0,
        })
    }

    /// Returns a Python list containing all items in the sequence.
    fn list(&self, py: Python<'_>) -> PyResult<Py<PyList>> {
        let list = PyList::empty(py);
        for item in &self.items {
            list.append(item)?;
        }
        Ok(list.into())
    }

    /// Returns a Python tuple containing all items in the sequence.
    fn tuple(&self, py: Python<'_>) -> PyResult<Py<PyTuple>> {
        let tuple = PyTuple::new(py, &self.items)?;
        Ok(tuple.into_py(py))
    }

    /// Returns a Python set containing all items in the sequence.
    fn set(&self, py: Python<'_>) -> PyResult<Py<PySet>> {
        let set = PySet::empty(py)?;
        for item in &self.items {
            set.add(item)?;
        }
        Ok(set.into())
    }

    /// Returns a new sequence where each element is a tuple of (index, value).
    #[pyo3(signature = (start_index=0))]
    fn enumerate(&self, py: Python<'_>, start_index: usize) -> PyResult<Self> {
        let mut result: Vec<PyObject> = Vec::with_capacity(self.items.len());

        for (i, item) in self.items.iter().enumerate() {
            let index = start_index + i;
            let pair = PyTuple::new(py, &[index.to_object(py), item.clone_ref(py)])?;
            result.push(pair.into_py(py));
        }

        Ok(PinqSeq {
            items: result,
            pointer: 0,
        })
    }

    /// Returns a Python iterator over the sequence.
    fn iter(&self, py: Python<'_>) -> PyResult<Py<PyIterator>> {
        let iter = PyIterator::from_object(&self.list(py)?.into_bound(py))?;
        Ok(iter.into())
    }

    /// Returns the number of items in the sequence.
    fn len(&self) -> usize {
        self.items.len()
    }

    /// Returns true if the sequence is empty.
    fn empty(&self) -> bool {
        self.items.is_empty()
    }

    /// Reverses the sequence.
    fn rev(&self, py: Python<'_>) -> Self {
        let mut new_items = Vec::with_capacity(self.items.len());
        for item in self.items.iter().rev() {
            new_items.push(item.clone_ref(py));
        }
        PinqSeq {
            items: new_items,
            pointer: 0,
        }
    }

    /// Returns a new sequence applying the given function to each item.
    fn select(&self, func: &Bound<'_, PyAny>) -> PyResult<Self> {
        let mut new_items = Vec::with_capacity(self.items.len());
        for item in &self.items {
            new_items.push(func.call1((item,))?.into());
        }
        Ok(PinqSeq {
            items: new_items,
            pointer: 0,
        })
    }

    /// Returns a new sequence filtering items based on the given predicate.
    #[pyo3(name = "where")]
    fn where_(&self, py: Python<'_>, predicate: &Bound<'_, PyAny>) -> PyResult<Self> {
        let mut new_items = Vec::with_capacity(self.items.len());
        for item in &self.items {
            if predicate.call1((item,))?.extract::<bool>()? {
                new_items.push(item.clone_ref(py));
            }
        }
        Ok(PinqSeq {
            items: new_items,
            pointer: 0,
        })
    }

    /// Returns a new sequence filtering items based on the given type.
    fn of_type(&self, py: Python<'_>, ty: &Bound<'_, PyType>) -> PyResult<Self> {
        let mut new_items = Vec::with_capacity(self.items.len());
        for item in &self.items {
            if item.bind(py).is_instance(ty)? {
                new_items.push(item.clone_ref(py));
            }
        }
        Ok(PinqSeq {
            items: new_items,
            pointer: 0,
        })
    }

    /// Orders the sequence based on the given key function.
    fn order_by(&self, py: Python<'_>, key: &Bound<'_, PyAny>) -> PyResult<Self> {
        let mut items_with_keys: Vec<(PyObject, PyObject)> = Vec::with_capacity(self.items.len());

        // Extract keys for each item
        for item in &self.items {
            let k = key.call1((item,))?.into_py(py);
            items_with_keys.push((item.clone_ref(py), k));
        }

        // Sort by the extracted keys
        items_with_keys.sort_by(|a, b| {
            let a_key = &a.1;
            let b_key = &b.1;

            match a_key.bind(py).rich_compare(b_key, CompareOp::Lt) {
                Ok(result) => {
                    if result.is_truthy().unwrap_or(false) {
                        std::cmp::Ordering::Less
                    } else {
                        match b_key.bind(py).rich_compare(a_key, CompareOp::Lt) {
                            Ok(result) => {
                                if result.is_truthy().unwrap_or(false) {
                                    std::cmp::Ordering::Greater
                                } else {
                                    std::cmp::Ordering::Equal
                                }
                            }
                            Err(_) => std::cmp::Ordering::Equal,
                        }
                    }
                }
                Err(_) => std::cmp::Ordering::Equal,
            }
        });

        // Extract just the items
        let sorted_items = items_with_keys.into_iter().map(|(item, _)| item).collect();

        Ok(PinqSeq {
            items: sorted_items,
            pointer: 0,
        })
    }

    fn group_by(&self, py: Python<'_>, key_func: &Bound<'_, PyAny>) -> PyResult<Self> {
        let mut groups: std::collections::HashMap<String, (PyObject, Vec<PyObject>)> =
            std::collections::HashMap::new();

        // Group items by their keys
        for item in &self.items {
            let key_obj = key_func.call1((item,))?;
            let key_str = format!("{:?}", key_obj.as_ref()); // Use string representation for hashing

            if !groups.contains_key(&key_str) {
                groups.insert(key_str.clone(), (key_obj.into_py(py), Vec::new()));
            }

            if let Some((_, group_items)) = groups.get_mut(&key_str) {
                group_items.push(item.clone_ref(py));
            }
        }

        // Build result tuples (key, PinqSeq of items)
        let mut result_items = Vec::new();

        for (_, (key, items)) in groups {
            // Create a PinqSeq for the grouped items
            let group_seq = PinqSeq {
                items: items,
                pointer: 0,
            };

            // Create a tuple of (key, group_seq)
            let group_tuple = PyTuple::new(py, &[key, group_seq.into_py(py)])?;

            result_items.push(group_tuple.into_py(py));
        }

        Ok(PinqSeq {
            items: result_items,
            pointer: 0,
        })
    }

    /// Returns the element at the given index, or the default value if the index is out of bounds.
    #[pyo3(signature = (index, default=None))]
    fn at(
        &self,
        py: Python<'_>,
        index: isize,
        default: Option<&Bound<'_, PyAny>>,
    ) -> PyResult<PyObject> {
        let len = self.items.len() as isize;
        let actual_index = if index < 0 { len + index } else { index };

        if actual_index >= 0 && actual_index < len {
            Ok(self.items[actual_index as usize].clone_ref(py))
        } else if let Some(default_value) = default {
            Ok(default_value.to_object(py))
        } else {
            // Return None if no default is provided
            Ok(py.None())
        }
    }

    #[pyo3(signature = (default=None))]
    /// Returns the first element in the sequence, or the default value if the sequence is empty.
    fn first(&self, py: Python<'_>, default: Option<&Bound<'_, PyAny>>) -> PyResult<PyObject> {
        if !self.items.is_empty() {
            Ok(self.items[0].clone_ref(py))
        } else if let Some(default_value) = default {
            Ok(default_value.to_object(py))
        } else {
            // Return None if no default is provided
            Ok(py.None())
        }
    }

    /// Returns the last element in the sequence, or the default value if the sequence is empty.
    #[pyo3(signature = (default=None))]
    fn last(&self, py: Python<'_>, default: Option<&Bound<'_, PyAny>>) -> PyResult<PyObject> {
        if !self.items.is_empty() {
            let last_index = self.items.len() - 1;
            Ok(self.items[last_index].clone_ref(py))
        } else if let Some(default_value) = default {
            Ok(default_value.to_object(py))
        } else {
            // Return None if no default is provided
            Ok(py.None())
        }
    }

    /// Adds an item to the end of the sequence.
    fn append(&self, py: Python<'_>, item: &Bound<'_, PyAny>) -> PyResult<Self> {
        // Create a new vector with all existing items
        let mut new_items = self
            .items
            .iter()
            .map(|existing| existing.clone_ref(py))
            .collect::<Vec<PyObject>>();

        // Add the new item to the end
        new_items.push(item.to_object(py));

        // Return a new PinqSeq with the updated items
        Ok(PinqSeq {
            items: new_items,
            pointer: self.pointer,
        })
    }

    /// Adds an item to the beginning of the sequence.
    fn prepend(&self, py: Python<'_>, item: &Bound<'_, PyAny>) -> PyResult<Self> {
        // Create a new vector starting with the new item
        let mut new_items = vec![item.to_object(py)];

        // Add all existing items
        new_items.extend(self.items.iter().map(|existing| existing.clone_ref(py)));

        // Return a new PinqSeq with the updated items
        Ok(PinqSeq {
            items: new_items,
            pointer: self.pointer,
        })
    }

    /// Joins this sequence with another sequence based on matching keys.
    /// outer_key_func extracts keys from this sequence.
    /// inner_key_func extracts keys from the input sequence.
    /// Returns a new sequence with pairs of matching elements.
    fn join(
        &self,
        py: Python<'_>,
        other: &Bound<'_, PyAny>,
        outer_key_func: &Bound<'_, PyAny>,
        inner_key_func: &Bound<'_, PyAny>,
    ) -> PyResult<Self> {
        // Convert the input to a Vec<PyObject>
        let inner_items = if other.is_instance_of::<PinqSeq>() {
            // If other is a PinqSeq
            let pinq_seq = other.extract::<Py<PinqSeq>>()?;
            let borrowed = pinq_seq.borrow(py);
            borrowed
                .items
                .iter()
                .map(|item| item.clone_ref(py))
                .collect::<Vec<PyObject>>()
        } else if other.is_instance_of::<PyList>() {
            // If other is a list
            let list = other.downcast::<PyList>()?;
            let mut items = Vec::with_capacity(list.len());
            for item in list.iter() {
                items.push(item.into());
            }
            items
        } else if other.is_instance_of::<PyTuple>() {
            // If other is a tuple
            let tuple = other.downcast::<PyTuple>()?;
            let mut items = Vec::with_capacity(tuple.len());
            for item in tuple.iter() {
                items.push(item.into());
            }
            items
        } else {
            return Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "Expected PinqSeq, list, or tuple",
            ));
        };

        // Create a hashmap of inner items grouped by their keys
        let mut inner_map: std::collections::HashMap<String, Vec<PyObject>> =
            std::collections::HashMap::new();

        for item in &inner_items {
            let key_obj = inner_key_func.call1((item,))?;
            let key_str = format!("{:?}", key_obj); // Use string representation for hashing

            if !inner_map.contains_key(&key_str) {
                inner_map.insert(key_str.clone(), Vec::new());
            }

            if let Some(group_items) = inner_map.get_mut(&key_str) {
                group_items.push(item.clone_ref(py));
            }
        }

        // Now join with the outer items
        let mut result_items = Vec::new();

        for outer_item in &self.items {
            let outer_key = outer_key_func.call1((outer_item,))?;
            let outer_key_str = format!("{:?}", outer_key);

            if let Some(matching_inner_items) = inner_map.get(&outer_key_str) {
                for inner_item in matching_inner_items {
                    // Create tuple for the joined result
                    let joined_pair =
                        PyTuple::new(py, &[outer_item.clone_ref(py), inner_item.clone_ref(py)])?;
                    result_items.push(joined_pair.into_py(py));
                }
            }
        }

        Ok(PinqSeq {
            items: result_items,
            pointer: 0,
        })
    }

    /// Returns a new sequence with duplicate elements removed.
    fn distinct(&self, py: Python<'_>) -> PyResult<Self> {
        if self.items.len() <= 1 {
            // If we have 0 or 1 items, just return a copy of the sequence
            return Ok(PinqSeq {
                items: self.items.iter().map(|item| item.clone_ref(py)).collect(),
                pointer: 0,
            });
        }

        let mut result: Vec<PyObject> = Vec::new();

        // For each item in the original sequence
        'outer: for item in &self.items {
            // Check if this item is already in our result
            for existing in &result {
                // Use Python's equality comparison
                let is_equal = match existing.bind(py).rich_compare(item, CompareOp::Eq) {
                    Ok(result) => result.is_truthy()?,
                    Err(_) => false,
                };

                if is_equal {
                    // Skip this item, it's already in our result
                    continue 'outer;
                }
            }

            // If we get here, this item isn't in the result yet
            result.push(item.clone_ref(py));
        }

        Ok(PinqSeq {
            items: result,
            pointer: 0,
        })
    }

    /// Concatenates this sequence with another sequence, list, or tuple.
    fn concat(&self, py: Python<'_>, other: &Bound<'_, PyAny>) -> PyResult<Self> {
        // Create a new sequence with all items from this sequence
        let mut new_items: Vec<PyObject> =
            self.items.iter().map(|item| item.clone_ref(py)).collect();

        // Add items from the other collection
        if other.is_instance_of::<PinqSeq>() {
            // If other is a PinqSeq
            let pinq_seq = other.extract::<Py<PinqSeq>>()?;
            let borrowed = pinq_seq.borrow(py);
            for item in &borrowed.items {
                new_items.push(item.clone_ref(py));
            }
        } else if other.is_instance_of::<PyList>() {
            // If other is a list
            let list = other.downcast::<PyList>()?;
            for item in list.iter() {
                new_items.push(item.into());
            }
        } else if other.is_instance_of::<PyTuple>() {
            // If other is a tuple
            let tuple = other.downcast::<PyTuple>()?;
            for item in tuple.iter() {
                new_items.push(item.into());
            }
        } else {
            return Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "Expected PinqSeq, list, or tuple for concatenation",
            ));
        }

        Ok(PinqSeq {
            items: new_items,
            pointer: 0,
        })
    }

    /// Returns a new sequence with elements from both sequences, removing duplicates.
    fn union(&self, py: Python<'_>, other: &Bound<'_, PyAny>) -> PyResult<Self> {
        // First, create a sequence with all items from this sequence
        let mut result = self.distinct(py)?;

        // Get items from the other collection
        let other_items: Vec<PyObject> = if other.is_instance_of::<PinqSeq>() {
            let pinq_seq = other.extract::<Py<PinqSeq>>()?;
            let borrowed = pinq_seq.borrow(py);
            borrowed
                .items
                .iter()
                .map(|item| item.clone_ref(py))
                .collect()
        } else if other.is_instance_of::<PyList>() {
            let list = other.downcast::<PyList>()?;
            list.iter().map(|item| item.to_object(py)).collect()
        } else if other.is_instance_of::<PyTuple>() {
            let tuple = other.downcast::<PyTuple>()?;
            tuple.iter().map(|item| item.to_object(py)).collect()
        } else {
            return Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "Expected PinqSeq, list, or tuple for union",
            ));
        };

        // Create a temporary PinqSeq with other items
        let other_seq = PinqSeq {
            items: other_items,
            pointer: 0,
        };

        // Get distinct items from other sequence
        let other_distinct = other_seq.distinct(py)?;

        // For each distinct item in the other sequence
        'outer: for other_item in &other_distinct.items {
            // Check if this item exists in our result
            for existing in &result.items {
                // Use Python's equality comparison
                let is_equal = match existing.bind(py).rich_compare(other_item, CompareOp::Eq) {
                    Ok(result) => result.is_truthy()?,
                    Err(_) => false,
                };

                if is_equal {
                    // Skip this item, it's already in our result
                    continue 'outer;
                }
            }

            // If we get here, the item isn't in the result yet
            result.items.push(other_item.clone_ref(py));
        }

        Ok(result)
    }

    /// Returns a new sequence with elements that exist in both sequences.
    fn intersect(&self, py: Python<'_>, other: &Bound<'_, PyAny>) -> PyResult<Self> {
        // Get items from the other collection
        let other_items: Vec<PyObject> = if other.is_instance_of::<PinqSeq>() {
            let pinq_seq = other.extract::<Py<PinqSeq>>()?;
            let borrowed = pinq_seq.borrow(py);
            borrowed
                .items
                .iter()
                .map(|item| item.clone_ref(py))
                .collect()
        } else if other.is_instance_of::<PyList>() {
            let list = other.downcast::<PyList>()?;
            list.iter().map(|item| item.to_object(py)).collect()
        } else if other.is_instance_of::<PyTuple>() {
            let tuple = other.downcast::<PyTuple>()?;
            tuple.iter().map(|item| item.to_object(py)).collect()
        } else {
            return Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "Expected PinqSeq, list, or tuple for intersection",
            ));
        };

        let mut result: Vec<PyObject> = Vec::new();

        // Create a temporary PinqSeq with other items and get the distinct items
        let other_seq = PinqSeq {
            items: other_items,
            pointer: 0,
        };
        let other_distinct = other_seq.distinct(py)?;

        // Get distinct items from this sequence
        let self_distinct = self.distinct(py)?;

        // For each distinct item in this sequence
        for self_item in &self_distinct.items {
            // Check if this item exists in the other sequence
            for other_item in &other_distinct.items {
                // Use Python's equality comparison
                let is_equal = match self_item.bind(py).rich_compare(other_item, CompareOp::Eq) {
                    Ok(result) => result.is_truthy()?,
                    Err(_) => false,
                };

                if is_equal {
                    // Add this item to the result
                    result.push(self_item.clone_ref(py));
                    break;
                }
            }
        }

        Ok(PinqSeq {
            items: result,
            pointer: 0,
        })
    }

    /// Returns a new sequence with elements from this sequence that don't exist in the other sequence.
    fn differ(&self, py: Python<'_>, other: &Bound<'_, PyAny>) -> PyResult<Self> {
        // Get items from the other collection
        let other_items: Vec<PyObject> = if other.is_instance_of::<PinqSeq>() {
            let pinq_seq = other.extract::<Py<PinqSeq>>()?;
            let borrowed = pinq_seq.borrow(py);
            borrowed
                .items
                .iter()
                .map(|item| item.clone_ref(py))
                .collect()
        } else if other.is_instance_of::<PyList>() {
            let list = other.downcast::<PyList>()?;
            list.iter().map(|item| item.to_object(py)).collect()
        } else if other.is_instance_of::<PyTuple>() {
            let tuple = other.downcast::<PyTuple>()?;
            tuple.iter().map(|item| item.to_object(py)).collect()
        } else {
            return Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "Expected PinqSeq, list, or tuple for except operation",
            ));
        };

        let mut result: Vec<PyObject> = Vec::new();

        // Create a temporary PinqSeq with other items and get the distinct items
        let other_seq = PinqSeq {
            items: other_items,
            pointer: 0,
        };
        let other_distinct = other_seq.distinct(py)?;

        // Get distinct items from this sequence
        let self_distinct = self.distinct(py)?;

        // For each distinct item in this sequence
        'outer: for self_item in &self_distinct.items {
            // Check if this item exists in the other sequence
            for other_item in &other_distinct.items {
                // Use Python's equality comparison
                let is_equal = match self_item.bind(py).rich_compare(other_item, CompareOp::Eq) {
                    Ok(result) => result.is_truthy()?,
                    Err(_) => false,
                };

                if is_equal {
                    // Skip this item, it exists in the other sequence
                    continue 'outer;
                }
            }

            // If we get here, the item doesn't exist in the other sequence
            result.push(self_item.clone_ref(py));
        }

        Ok(PinqSeq {
            items: result,
            pointer: 0,
        })
    }

    /// Skips the next n items in the sequence, advancing the pointer.
    fn skip(&mut self, py: Python<'_>, n: usize) -> PyResult<Self> {
        let new_pointer = std::cmp::min(self.pointer + n, self.items.len());
        let cloned_items = self.items.iter().map(|item| item.clone_ref(py)).collect();
        Ok(PinqSeq {
            items: cloned_items,
            pointer: new_pointer,
        })
    }

    /// Restarts the sequence by resetting the pointer to zero.
    fn restart(&self, py: Python<'_>) -> PyResult<Self> {
        let cloned_items = self.items.iter().map(|item| item.clone_ref(py)).collect();
        Ok(PinqSeq {
            items: cloned_items,
            pointer: 0,
        })
    }

    /// Takes the next n items from the current position.
    /// Returns a tuple containing:
    /// - A new sequence with the next n items (or fewer if less are available)
    /// - The original sequence with the pointer advanced
    fn take(&self, py: Python<'_>, n: usize) -> PyResult<Py<PyTuple>> {
        let available_items = self.items.len() - self.pointer;
        let actual_take = std::cmp::min(n, available_items);

        // Create a new sequence with the taken items
        let taken_items: Vec<PyObject> = self.items[self.pointer..(self.pointer + actual_take)]
            .iter()
            .map(|item| item.clone_ref(py))
            .collect();

        let taken_seq = PinqSeq {
            items: taken_items,
            pointer: 0,
        };

        // Create a copy of self with advanced pointer
        let advanced_seq = PinqSeq {
            items: self.items.iter().map(|item| item.clone_ref(py)).collect(),
            pointer: self.pointer + actual_take,
        };

        // Return a tuple with (taken_seq, advanced_seq)
        let result = PyTuple::new(py, &[taken_seq.into_py(py), advanced_seq.into_py(py)])?;

        Ok(result.into())
    }

    /// Combines elements from this sequence with elements from another sequence.
    /// If until_exhausted is True, continues until both sequences are exhausted,
    /// filling in None for missing values. If False (default), stops when the shorter sequence is exhausted.
    #[pyo3(signature = (other, until_exhausted=false))]
    fn zip(
        &self,
        py: Python<'_>,
        other: &Bound<'_, PyAny>,
        until_exhausted: bool,
    ) -> PyResult<Self> {
        // Convert the input to a Vec<PyObject>
        let other_items: Vec<PyObject> = if other.is_instance_of::<PinqSeq>() {
            // If other is a PinqSeq
            let pinq_seq = other.extract::<Py<PinqSeq>>()?;
            let borrowed = pinq_seq.borrow(py);
            borrowed
                .items
                .iter()
                .map(|item| item.clone_ref(py))
                .collect()
        } else if other.is_instance_of::<PyList>() {
            // If other is a list
            let list = other.downcast::<PyList>()?;
            list.iter().map(|item| item.to_object(py)).collect()
        } else if other.is_instance_of::<PyTuple>() {
            // If other is a tuple
            let tuple = other.downcast::<PyTuple>()?;
            tuple.iter().map(|item| item.to_object(py)).collect()
        } else {
            return Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "Expected PinqSeq, list, or tuple for zip operation",
            ));
        };

        let mut result: Vec<PyObject> = Vec::new();

        if until_exhausted {
            // Continue until both sequences are exhausted
            let max_len = std::cmp::max(self.items.len(), other_items.len());
            for i in 0..max_len {
                let self_item = if i < self.items.len() {
                    self.items[i].clone_ref(py)
                } else {
                    py.None().into()
                };

                let other_item = if i < other_items.len() {
                    other_items[i].clone_ref(py)
                } else {
                    py.None().into()
                };

                let pair = PyTuple::new(py, &[self_item, other_item])?;
                result.push(pair.into_py(py));
            }
        } else {
            // Stop when the shorter sequence is exhausted
            let min_len = std::cmp::min(self.items.len(), other_items.len());
            for i in 0..min_len {
                let self_item = self.items[i].clone_ref(py);
                let other_item = other_items[i].clone_ref(py);

                let pair = PyTuple::new(py, &[self_item, other_item])?;
                result.push(pair.into_py(py));
            }
        }

        Ok(PinqSeq {
            items: result,
            pointer: 0,
        })
    }

    /// Combines elements from this sequence with elements from other sequences.
    /// Returns a new sequence with tuples containing corresponding elements from each sequence.
    /// If until_exhausted is True, continues until all sequences are exhausted,
    /// filling in None for missing values. If False (default), stops when the shortest sequence is exhausted.
    #[pyo3(signature = (others, until_exhausted=false))]
    fn zips(
        &self,
        py: Python<'_>,
        others: &Bound<'_, PyList>,
        until_exhausted: bool,
    ) -> PyResult<Self> {
        // Convert each input sequence to a Vec<PyObject>
        let mut all_sequences: Vec<Vec<PyObject>> = Vec::new();

        // Add this sequence as the first one
        all_sequences.push(self.items.iter().map(|item| item.clone_ref(py)).collect());

        // Process each of the other sequences
        for other in others.iter() {
            let other_items: Vec<PyObject> = if other.is_instance_of::<PinqSeq>() {
                // If other is a PinqSeq
                let pinq_seq = other.extract::<Py<PinqSeq>>()?;
                let borrowed = pinq_seq.borrow(py);
                borrowed
                    .items
                    .iter()
                    .map(|item| item.clone_ref(py))
                    .collect()
            } else if other.is_instance_of::<PyList>() {
                // If other is a list
                let list = other.downcast::<PyList>()?;
                list.iter().map(|item| item.to_object(py)).collect()
            } else if other.is_instance_of::<PyTuple>() {
                // If other is a tuple
                let tuple = other.downcast::<PyTuple>()?;
                tuple.iter().map(|item| item.to_object(py)).collect()
            } else {
                return Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                    "Expected sequences (PinqSeq, list, or tuple) for zip operation",
                ));
            };

            all_sequences.push(other_items);
        }

        let mut result: Vec<PyObject> = Vec::new();

        if until_exhausted {
            // Continue until all sequences are exhausted
            // Find the maximum length of all sequences
            let max_len = all_sequences.iter().map(|seq| seq.len()).max().unwrap_or(0);

            // For each position
            for i in 0..max_len {
                // Create a tuple with elements from each sequence at this position, or None if out of bounds
                let mut tuple_items: Vec<PyObject> = Vec::new();

                for seq in &all_sequences {
                    let item = if i < seq.len() {
                        seq[i].clone_ref(py)
                    } else {
                        py.None().into()
                    };
                    tuple_items.push(item);
                }

                let tuple = PyTuple::new(py, &tuple_items)?;
                result.push(tuple.into_py(py));
            }
        } else {
            // Stop when the shortest sequence is exhausted
            // Find the minimum length of all sequences
            let min_len = all_sequences.iter().map(|seq| seq.len()).min().unwrap_or(0);

            // For each position up to the minimum length
            for i in 0..min_len {
                // Create a tuple with elements from each sequence at this position
                let mut tuple_items: Vec<PyObject> = Vec::new();

                for seq in &all_sequences {
                    tuple_items.push(seq[i].clone_ref(py));
                }

                let tuple = PyTuple::new(py, &tuple_items)?;
                result.push(tuple.into_py(py));
            }
        }

        Ok(PinqSeq {
            items: result,
            pointer: 0,
        })
    }

    fn flatten(&self, py: Python<'_>) -> PyResult<Self> {
        let mut result: Vec<PyObject> = Vec::new();

        // Helper function to check if an object is a sequence type we want to flatten
        fn is_sequence_type(obj: &Bound<'_, PyAny>) -> bool {
            obj.is_instance_of::<PinqSeq>()
                || obj.is_instance_of::<PyList>()
                || obj.is_instance_of::<PyTuple>()
        }

        // Helper function to recursively flatten sequences
        fn flatten_item(
            py: Python<'_>,
            item: &PyObject,
            result: &mut Vec<PyObject>,
        ) -> PyResult<()> {
            let bound_item = item.bind(py);

            if is_sequence_type(&bound_item) {
                let items_to_flatten: Vec<PyObject> = if bound_item.is_instance_of::<PinqSeq>() {
                    // Extract items from PinqSeq
                    let pinq_seq = bound_item.extract::<Py<PinqSeq>>()?;
                    let borrowed = pinq_seq.borrow(py);
                    borrowed.items.iter().map(|i| i.clone_ref(py)).collect()
                } else if bound_item.is_instance_of::<PyList>() {
                    // Extract items from list
                    let list = bound_item.downcast::<PyList>()?;
                    list.iter().map(|i| i.to_object(py)).collect()
                } else if bound_item.is_instance_of::<PyTuple>() {
                    // Extract items from tuple
                    let tuple = bound_item.downcast::<PyTuple>()?;
                    tuple.iter().map(|i| i.to_object(py)).collect()
                } else {
                    unreachable!(); // We've already checked all sequence types
                };

                // Recursively flatten each item in the sequence
                for nested_item in items_to_flatten {
                    flatten_item(py, &nested_item, result)?;
                }
            } else {
                // This is not a sequence to flatten, so add it directly
                result.push(item.clone_ref(py));
            }

            Ok(())
        }

        // Process each item in the sequence
        for item in &self.items {
            flatten_item(py, item, &mut result)?;
        }

        Ok(PinqSeq {
            items: result,
            pointer: 0,
        })
    }

    /// Returns the sum of all elements. Warns if non-numeric elements are present.
    fn sum(&self, py: Python<'_>) -> PyResult<PyObject> {
        if self.items.is_empty() {
            return Ok(py.None());
        }

        let mut sum_value = 0.0;
        let mut has_warning = false;

        for (i, item) in self.items.iter().enumerate() {
            match item.bind(py).extract::<f64>() {
                Ok(num) => sum_value += num,
                Err(_) => {
                    if !has_warning {
                        eprintln!(
                            "Warning: Non-numeric value found in sequence during sum operation"
                        );
                        has_warning = true;
                    }
                    eprintln!("  at index {}: {:?}", i, item.bind(py));
                }
            }
        }

        Ok(sum_value.to_object(py))
    }

    /// Returns the average of all elements. Warns if non-numeric elements are present.
    fn average(&self, py: Python<'_>) -> PyResult<PyObject> {
        if self.items.is_empty() {
            return Ok(py.None());
        }

        let mut sum_value = 0.0;
        let mut count = 0;
        let mut has_warning = false;

        for (i, item) in self.items.iter().enumerate() {
            match item.bind(py).extract::<f64>() {
                Ok(num) => {
                    sum_value += num;
                    count += 1;
                }
                Err(_) => {
                    if !has_warning {
                        eprintln!(
                            "Warning: Non-numeric value found in sequence during average operation"
                        );
                        has_warning = true;
                    }
                    eprintln!("  at index {}: {:?}", i, item.bind(py));
                }
            }
        }

        if count > 0 {
            Ok((sum_value / count as f64).to_object(py))
        } else {
            Ok(py.None())
        }
    }

    /// Returns the maximum value in the sequence. Warns if non-numeric elements are present.
    fn max(&self, py: Python<'_>) -> PyResult<PyObject> {
        if self.items.is_empty() {
            return Ok(py.None());
        }

        let mut max_value: Option<f64> = None;
        let mut has_warning = false;

        for (i, item) in self.items.iter().enumerate() {
            match item.bind(py).extract::<f64>() {
                Ok(num) => {
                    max_value = Some(match max_value {
                        Some(current_max) => {
                            if num > current_max {
                                num
                            } else {
                                current_max
                            }
                        }
                        None => num,
                    });
                }
                Err(_) => {
                    if !has_warning {
                        eprintln!(
                            "Warning: Non-numeric value found in sequence during max operation"
                        );
                        has_warning = true;
                    }
                    eprintln!("  at index {}: {:?}", i, item.bind(py));
                }
            }
        }

        match max_value {
            Some(value) => Ok(value.to_object(py)),
            None => Ok(py.None()),
        }
    }

    /// Returns the minimum value in the sequence. Warns if non-numeric elements are present.
    fn min(&self, py: Python<'_>) -> PyResult<PyObject> {
        if self.items.is_empty() {
            return Ok(py.None());
        }

        let mut min_value: Option<f64> = None;
        let mut has_warning = false;

        for (i, item) in self.items.iter().enumerate() {
            match item.bind(py).extract::<f64>() {
                Ok(num) => {
                    min_value = Some(match min_value {
                        Some(current_min) => {
                            if num < current_min {
                                num
                            } else {
                                current_min
                            }
                        }
                        None => num,
                    });
                }
                Err(_) => {
                    if !has_warning {
                        eprintln!(
                            "Warning: Non-numeric value found in sequence during min operation"
                        );
                        has_warning = true;
                    }
                    eprintln!("  at index {}: {:?}", i, item.bind(py));
                }
            }
        }

        match min_value {
            Some(value) => Ok(value.to_object(py)),
            None => Ok(py.None()),
        }
    }

    /// Attempts to cast all items in the sequence to the specified type.
    /// If silent is True, items that can't be cast will be skipped instead of raising an error.
    #[pyo3(signature = (ty, silent=false))]
    fn cast(&self, ty: &Bound<'_, PyType>, silent: bool) -> PyResult<Self> {
        let mut new_items = Vec::with_capacity(self.items.len());

        for (i, item) in self.items.iter().enumerate() {
            let result = ty.call1((item,));

            match result {
                Ok(cast_item) => {
                    new_items.push(cast_item.into());
                }
                Err(err) => {
                    if silent {
                        // Skip this item in silent mode
                        continue;
                    } else {
                        // Return detailed error message
                        return Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(format!(
                            "Failed to cast item at index {} to {}: {}",
                            i,
                            ty.getattr("__name__")?.extract::<String>()?,
                            err
                        )));
                    }
                }
            }
        }

        Ok(PinqSeq {
            items: new_items,
            pointer: 0,
        })
    }

    /// Creates a dictionary from the sequence using key_func to generate keys and value_func to generate values.
    fn to_dict(
        &self,
        py: Python<'_>,
        key_func: &Bound<'_, PyAny>,
        value_func: &Bound<'_, PyAny>,
    ) -> PyResult<PyObject> {
        // Import Python's dict type
        let dict = PyDict::new(py);

        // For each item in the sequence
        for item in &self.items {
            // Generate key and value by calling the provided functions
            let key = key_func.call1((item,))?;
            let value = value_func.call1((item,))?;

            // Set the key-value pair in the dictionary
            dict.set_item(key, value)?;
        }

        Ok(dict.into())
    }

    /// Applies an accumulator function over a sequence.
    /// The function should take two parameters: accumulator and item.
    #[pyo3(signature = (func, seed=None))]
    fn aggregate(
        &self,
        py: Python<'_>,
        func: &Bound<'_, PyAny>,
        seed: Option<&Bound<'_, PyAny>>,
    ) -> PyResult<PyObject> {
        if self.items.is_empty() {
            return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                "Cannot aggregate an empty sequence",
            ));
        }

        // Initialize the accumulator with the seed value or the first item
        let mut acc = if let Some(seed_value) = seed {
            seed_value.to_object(py)
        } else {
            self.items[0].clone_ref(py)
        };

        // Start from the beginning or second item based on whether a seed was provided
        let start_idx = if seed.is_some() { 0 } else { 1 };

        // Apply the accumulator function to each item
        for i in start_idx..self.items.len() {
            acc = func.call1((acc, &self.items[i]))?.to_object(py);
        }

        Ok(acc)
    }

    /// Skips elements as long as a condition is true.
    fn skip_while(&self, py: Python<'_>, predicate: &Bound<'_, PyAny>) -> PyResult<Self> {
        let mut skip_count = 0;

        // Count how many items to skip while the predicate is true
        for item in &self.items {
            if predicate.call1((item,))?.extract::<bool>()? {
                skip_count += 1;
            } else {
                // As soon as predicate is false for an item, stop counting
                break;
            }
        }

        let new_pointer = std::cmp::min(self.pointer + skip_count, self.items.len());

        // Create a new sequence with the pointer advanced
        let cloned_items = self.items.iter().map(|item| item.clone_ref(py)).collect();
        Ok(PinqSeq {
            items: cloned_items,
            pointer: new_pointer,
        })
    }

    /// Takes items from the current position as long as they satisfy the predicate.
    /// Returns a tuple containing:
    /// - A new sequence with the items that satisfy the predicate
    /// - The original sequence with the pointer advanced past those items
    fn take_while(&self, py: Python<'_>, predicate: &Bound<'_, PyAny>) -> PyResult<Py<PyTuple>> {
        let mut take_count = 0;

        // Count how many items to take while the predicate is true
        for i in self.pointer..self.items.len() {
            if predicate.call1((&self.items[i],))?.extract::<bool>()? {
                take_count += 1;
            } else {
                // As soon as predicate is false for an item, stop counting
                break;
            }
        }

        // Create a new sequence with the taken items
        let taken_items: Vec<PyObject> = self.items[self.pointer..(self.pointer + take_count)]
            .iter()
            .map(|item| item.clone_ref(py))
            .collect();

        let taken_seq = PinqSeq {
            items: taken_items,
            pointer: 0,
        };

        // Create a copy of self with advanced pointer
        let advanced_seq = PinqSeq {
            items: self.items.iter().map(|item| item.clone_ref(py)).collect(),
            pointer: self.pointer + take_count,
        };

        // Return a tuple with (taken_seq, advanced_seq)
        let result = PyTuple::new(py, &[taken_seq.into_py(py), advanced_seq.into_py(py)])?;

        Ok(result.into())
    }

    /// Returns a new sequence with elements having distinct values according to the key selector function.
    fn distinct_by(&self, py: Python<'_>, key_selector: &Bound<'_, PyAny>) -> PyResult<Self> {
        if self.items.len() <= 1 {
            // If we have 0 or 1 items, just return a copy of the sequence
            return Ok(PinqSeq {
                items: self.items.iter().map(|item| item.clone_ref(py)).collect(),
                pointer: 0,
            });
        }

        let mut result: Vec<PyObject> = Vec::new();
        let mut seen_keys: Vec<PyObject> = Vec::new();

        // For each item in the original sequence
        for item in &self.items {
            // Extract the key for this item
            let item_key = key_selector.call1((item,))?.to_object(py);

            // Check if this key is already seen
            let mut is_duplicate = false;
            for existing_key in &seen_keys {
                // Use Python's equality comparison
                let is_equal = match existing_key.bind(py).rich_compare(&item_key, CompareOp::Eq) {
                    Ok(result) => result.is_truthy()?,
                    Err(_) => false,
                };

                if is_equal {
                    // Skip this item, its key already exists
                    is_duplicate = true;
                    break;
                }
            }

            if !is_duplicate {
                // If key not seen yet, add the item to result and key to seen_keys
                seen_keys.push(item_key);
                result.push(item.clone_ref(py));
            }
        }

        Ok(PinqSeq {
            items: result,
            pointer: 0,
        })
    }

    /// Returns a new sequence with elements from this sequence whose keys don't exist in the other sequence.
    fn except_by(
        &self,
        py: Python<'_>,
        other: &Bound<'_, PyAny>,
        key_selector: &Bound<'_, PyAny>,
    ) -> PyResult<Self> {
        // Get items from the other collection
        let other_items: Vec<PyObject> = if other.is_instance_of::<PinqSeq>() {
            let pinq_seq = other.extract::<Py<PinqSeq>>()?;
            let borrowed = pinq_seq.borrow(py);
            borrowed
                .items
                .iter()
                .map(|item| item.clone_ref(py))
                .collect()
        } else if other.is_instance_of::<PyList>() {
            let list = other.downcast::<PyList>()?;
            list.iter().map(|item| item.to_object(py)).collect()
        } else if other.is_instance_of::<PyTuple>() {
            let tuple = other.downcast::<PyTuple>()?;
            tuple.iter().map(|item| item.to_object(py)).collect()
        } else {
            return Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "Expected PinqSeq, list, or tuple for except_by operation",
            ));
        };

        // Extract keys from other sequence
        let mut other_keys: Vec<PyObject> = Vec::new();
        for item in &other_items {
            other_keys.push(key_selector.call1((item,))?.to_object(py));
        }

        // Filter this sequence based on keys
        let mut result: Vec<PyObject> = Vec::new();

        for item in &self.items {
            let item_key = key_selector.call1((item,))?.to_object(py);

            // Check if this key exists in other_keys
            let mut exists_in_other = false;
            for other_key in &other_keys {
                let is_equal = match other_key.bind(py).rich_compare(&item_key, CompareOp::Eq) {
                    Ok(result) => result.is_truthy()?,
                    Err(_) => false,
                };

                if is_equal {
                    exists_in_other = true;
                    break;
                }
            }

            if !exists_in_other {
                // Add this item if its key doesn't exist in other sequence
                result.push(item.clone_ref(py));
            }
        }

        // Return distinct items by key to ensure uniqueness in result
        let temp_seq = PinqSeq {
            items: result,
            pointer: 0,
        };

        temp_seq.distinct_by(py, key_selector)
    }

    /// Returns a new sequence with elements that exist in both sequences, comparing by keys.
    fn intersect_by(
        &self,
        py: Python<'_>,
        other: &Bound<'_, PyAny>,
        key_selector: &Bound<'_, PyAny>,
    ) -> PyResult<Self> {
        // Get items from the other collection
        let other_items: Vec<PyObject> = if other.is_instance_of::<PinqSeq>() {
            let pinq_seq = other.extract::<Py<PinqSeq>>()?;
            let borrowed = pinq_seq.borrow(py);
            borrowed
                .items
                .iter()
                .map(|item| item.clone_ref(py))
                .collect()
        } else if other.is_instance_of::<PyList>() {
            let list = other.downcast::<PyList>()?;
            list.iter().map(|item| item.to_object(py)).collect()
        } else if other.is_instance_of::<PyTuple>() {
            let tuple = other.downcast::<PyTuple>()?;
            tuple.iter().map(|item| item.to_object(py)).collect()
        } else {
            return Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "Expected PinqSeq, list, or tuple for intersect_by operation",
            ));
        };

        // Extract keys from other sequence
        let mut other_keys: Vec<PyObject> = Vec::new();
        for item in &other_items {
            other_keys.push(key_selector.call1((item,))?.to_object(py));
        }

        // Filter this sequence based on keys that also exist in other sequence
        let mut result: Vec<PyObject> = Vec::new();

        for item in &self.items {
            let item_key = key_selector.call1((item,))?.to_object(py);

            // Check if this key exists in other_keys
            for other_key in &other_keys {
                let is_equal = match other_key.bind(py).rich_compare(&item_key, CompareOp::Eq) {
                    Ok(result) => result.is_truthy()?,
                    Err(_) => false,
                };

                if is_equal {
                    // Add this item if its key exists in other sequence
                    result.push(item.clone_ref(py));
                    break;
                }
            }
        }

        // Return distinct items by key to ensure uniqueness in result
        let temp_seq = PinqSeq {
            items: result,
            pointer: 0,
        };

        temp_seq.distinct_by(py, key_selector)
    }

    /// Returns a new sequence with elements from both sequences, removing duplicates based on keys.
    fn union_by(
        &self,
        py: Python<'_>,
        other: &Bound<'_, PyAny>,
        key_selector: &Bound<'_, PyAny>,
    ) -> PyResult<Self> {
        // Get items from the other collection
        let other_items: Vec<PyObject> = if other.is_instance_of::<PinqSeq>() {
            let pinq_seq = other.extract::<Py<PinqSeq>>()?;
            let borrowed = pinq_seq.borrow(py);
            borrowed
                .items
                .iter()
                .map(|item| item.clone_ref(py))
                .collect()
        } else if other.is_instance_of::<PyList>() {
            let list = other.downcast::<PyList>()?;
            list.iter().map(|item| item.to_object(py)).collect()
        } else if other.is_instance_of::<PyTuple>() {
            let tuple = other.downcast::<PyTuple>()?;
            tuple.iter().map(|item| item.to_object(py)).collect()
        } else {
            return Err(PyErr::new::<pyo3::exceptions::PyTypeError, _>(
                "Expected PinqSeq, list, or tuple for union_by operation",
            ));
        };

        // Create a combined sequence of all items
        let mut all_items = self
            .items
            .iter()
            .map(|item| item.clone_ref(py))
            .collect::<Vec<PyObject>>();
        all_items.extend(other_items);

        // Create a temporary sequence with all items
        let combined_seq = PinqSeq {
            items: all_items,
            pointer: 0,
        };

        // Return distinct items by key to ensure uniqueness
        combined_seq.distinct_by(py, key_selector)
    }

    /// Returns the element with the minimum value as determined by the key selector.
    fn min_by(&self, py: Python<'_>, key_selector: &Bound<'_, PyAny>) -> PyResult<PyObject> {
        if self.items.is_empty() {
            return Ok(py.None());
        }

        let mut min_item = &self.items[0];
        let mut min_key = key_selector.call1((min_item,))?;

        // Compare each item's key with the current minimum
        for i in 1..self.items.len() {
            let item = &self.items[i];
            let key = key_selector.call1((item,))?;

            // Check if this key is less than the current min_key
            if key.is_instance_of::<PyAny>() {
                match key.rich_compare(&min_key, CompareOp::Lt)?.is_truthy() {
                    Ok(true) => {
                        min_item = item;
                        min_key = key;
                    }
                    _ => {}
                }
            }
        }

        Ok(min_item.clone_ref(py))
    }

    /// Returns the element with the maximum value as determined by the key selector.
    fn max_by(&self, py: Python<'_>, key_selector: &Bound<'_, PyAny>) -> PyResult<PyObject> {
        if self.items.is_empty() {
            return Ok(py.None());
        }

        let mut max_item = &self.items[0];
        let mut max_key = key_selector.call1((max_item,))?;

        // Compare each item's key with the current maximum
        for i in 1..self.items.len() {
            let item = &self.items[i];
            let key = key_selector.call1((item,))?;

            // Check if this key is greater than the current max_key
            if key.is_instance_of::<PyAny>() {
                match key.rich_compare(&max_key, CompareOp::Gt)?.is_truthy() {
                    Ok(true) => {
                        max_item = item;
                        max_key = key;
                    }
                    _ => {}
                }
            }
        }

        Ok(max_item.clone_ref(py))
    }

    /// Splits the sequence into chunks of the specified size.
    /// Returns a new sequence containing subsequences (as PinqSeq objects) of the specified size.
    /// The last chunk may contain fewer elements if the sequence length is not divisible by the chunk_size.
    fn chunk(&self, py: Python<'_>, chunk_size: usize) -> PyResult<Self> {
        if chunk_size == 0 {
            return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                "Chunk size must be greater than 0",
            ));
        }

        let mut result: Vec<PyObject> = Vec::new();
        let num_chunks = (self.items.len() + chunk_size - 1) / chunk_size; // ceiling division

        for i in 0..num_chunks {
            let start = i * chunk_size;
            let end = std::cmp::min(start + chunk_size, self.items.len());

            // Create a new PinqSeq for this chunk
            let chunk_items: Vec<PyObject> = self.items[start..end]
                .iter()
                .map(|item| item.clone_ref(py))
                .collect();

            let chunk_seq = PinqSeq {
                items: chunk_items,
                pointer: 0,
            };

            result.push(chunk_seq.into_py(py));
        }

        Ok(PinqSeq {
            items: result,
            pointer: 0,
        })
    }
}

/// C#-like querying module
#[pymodule]
fn pinq(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<PinqSeq>()?;
    Ok(())
}
