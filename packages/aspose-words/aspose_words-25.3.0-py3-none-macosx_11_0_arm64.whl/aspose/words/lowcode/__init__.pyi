﻿import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List
from enum import Enum

class Comparer:
    """Provides methods intended to compare documents."""
    
    @overload
    @staticmethod
    def compare(v1: str, v2: str, output_file_name: str, author: str, date_time: datetime.datetime) -> None:
        """Compares two documents and saves the differences to the specified output file,
        producing changes as a number of edit and format revisions.
        
        :param v1: The original document.
        :param v2: The modified document.
        :param output_file_name: The output file name.
        :param author: Initials of the author to use for revisions.
        :param date_time: The date and time to use for revisions."""
        ...
    
    @overload
    @staticmethod
    def compare(v1: str, v2: str, output_file_name: str, save_format: aspose.words.SaveFormat, author: str, date_time: datetime.datetime) -> None:
        """Compares two documents and saves the differences to the specified output file in the provided save format,
        producing changes as a number of edit and format revisions.
        
        :param v1: The original document.
        :param v2: The modified document.
        :param output_file_name: The output file name.
        :param save_format: The output's save format.
        :param author: Initials of the author to use for revisions.
        :param date_time: The date and time to use for revisions."""
        ...
    
    @overload
    @staticmethod
    def compare(v1: str, v2: str, output_file_name: str, author: str, date_time: datetime.datetime, compare_options: aspose.words.comparing.CompareOptions) -> None:
        """Compares two documents with additional options and saves the differences to the specified output file,
        producing changes as a number of edit and format revisions.
        
        :param v1: The original document.
        :param v2: The modified document.
        :param output_file_name: The output file name.
        :param author: Initials of the author to use for revisions.
        :param date_time: The date and time to use for revisions.
        :param compare_options: Document comparison options."""
        ...
    
    @overload
    @staticmethod
    def compare(v1: str, v2: str, output_file_name: str, save_format: aspose.words.SaveFormat, author: str, date_time: datetime.datetime, compare_options: aspose.words.comparing.CompareOptions) -> None:
        """Compares two documents with additional options and saves the differences to the specified output file in the provided save format,
        producing changes as a number of edit and format revisions.
        
        :param v1: The original document.
        :param v2: The modified document.
        :param output_file_name: The output file name.
        :param save_format: The output's save format.
        :param author: Initials of the author to use for revisions.
        :param date_time: The date and time to use for revisions.
        :param compare_options: Document comparison options."""
        ...
    
    @overload
    @staticmethod
    def compare(v1: str, v2: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions, author: str, date_time: datetime.datetime, compare_options: aspose.words.comparing.CompareOptions) -> None:
        """Compares two documents with additional options and saves the differences to the specified output file in the provided save format,
        producing changes as a number of edit and format revisions.
        
        :param v1: The original document.
        :param v2: The modified document.
        :param output_file_name: The output file name.
        :param save_options: The output's save options.
        :param author: Initials of the author to use for revisions.
        :param date_time: The date and time to use for revisions.
        :param compare_options: Document comparison options."""
        ...
    
    @overload
    @staticmethod
    def compare(v1: io.BytesIO, v2: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, author: str, date_time: datetime.datetime) -> None:
        """Compares two documents loaded from streams and saves the differences to the provided output stream in the specified save format,
        producing changes as a number of edit and format revisions.
        
        :param v1: The original document.
        :param v2: The modified document.
        :param output_stream: The output stream.
        :param save_format: The output's save format.
        :param author: Initials of the author to use for revisions.
        :param date_time: The date and time to use for revisions."""
        ...
    
    @overload
    @staticmethod
    def compare(v1: io.BytesIO, v2: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, author: str, date_time: datetime.datetime, compare_options: aspose.words.comparing.CompareOptions) -> None:
        """Compares two documents loaded from streams with additional options and saves the differences to the provided output stream in the specified save format,
        producing changes as a number of edit and format revisions.
        
        :param v1: The original document.
        :param v2: The modified document.
        :param output_stream: The output stream.
        :param save_format: The output's save format.
        :param author: Initials of the author to use for revisions.
        :param date_time: The date and time to use for revisions.
        :param compare_options: Document comparison options."""
        ...
    
    @overload
    @staticmethod
    def compare(v1: io.BytesIO, v2: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions, author: str, date_time: datetime.datetime, compare_options: aspose.words.comparing.CompareOptions) -> None:
        """Compares two documents loaded from streams with additional options and saves the differences to the provided output stream in the specified save format,
        producing changes as a number of edit and format revisions.
        
        :param v1: The original document.
        :param v2: The modified document.
        :param output_stream: The output stream.
        :param save_options: The output's save options.
        :param author: Initials of the author to use for revisions.
        :param date_time: The date and time to use for revisions.
        :param compare_options: Document comparison options."""
        ...
    
    ...

class Converter:
    """Represents a group of methods intended to convert a variety of different types of documents using a single line of code.
    
    The specified input and output files or streams, along with the desired save format,
    are used to convert the given input document of the one format into the output document
    of the other specified format.
    
    The convert functionality supports over 35+ different file formats.
    
    The :meth:`Converter.convert_to_images` group of methods are designed to transform documents into images,
    with each page being converted into a separate image file. These methods also convert PDF documents directly to fixed-page formats
    without loading them into the document model, which enhances both performance and accuracy.
    
    With :attr:`aspose.words.saving.ImageSaveOptions.page_set`, you can specify a particular set of pages to convert into images."""
    
    @overload
    @staticmethod
    def convert(input_file: str, output_file: str) -> None:
        """Converts the given input document into the output document using specified input output file names and its extensions.
        
        :param input_file: The input file name.
        :param output_file: The output file name."""
        ...
    
    @overload
    @staticmethod
    def convert(input_file: str, output_file: str, save_format: aspose.words.SaveFormat) -> None:
        """Converts the given input document into the output document using specified input output file names and the final document format.
        
        :param input_file: The input file name.
        :param output_file: The output file name.
        :param save_format: The save format."""
        ...
    
    @overload
    @staticmethod
    def convert(input_file: str, output_file: str, save_options: aspose.words.saving.SaveOptions) -> None:
        """Converts the given input document into the output document using specified input output file names and save options.
        
        :param input_file: The input file name.
        :param output_file: The output file name.
        :param save_options: The save options."""
        ...
    
    @overload
    @staticmethod
    def convert(input_file: str, load_options: aspose.words.loading.LoadOptions, output_file: str, save_options: aspose.words.saving.SaveOptions) -> None:
        """Converts the given input document into the output document using specified input output file names its load/save options.
        
        :param input_file: The input file name.
        :param load_options: The input document load options.
        :param output_file: The output file name.
        :param save_options: The save options."""
        ...
    
    @overload
    @staticmethod
    def convert(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat) -> None:
        """Converts the given input document into a single output document using specified input and output streams.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_format: The save format."""
        ...
    
    @overload
    @staticmethod
    def convert(input_stream: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions) -> None:
        """Converts the given input document into a single output document using specified input and output streams.
        
        :param input_stream: The input streams.
        :param output_stream: The output stream.
        :param save_options: The save options."""
        ...
    
    @overload
    @staticmethod
    def convert(input_stream: io.BytesIO, load_options: aspose.words.loading.LoadOptions, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions) -> None:
        """Converts the given input document into a single output document using specified input and output streams.
        
        :param input_stream: The input streams.
        :param load_options: The input document load options.
        :param output_stream: The output stream.
        :param save_options: The save options."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_file: str, output_file: str) -> None:
        """Converts the pages of the specified input file to image files.
        
        :param input_file: The input file name.
        :param output_file: The output file name used to generate file name for page images using rule "outputFile_pageIndex.extension""""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_file: str, output_file: str, save_format: aspose.words.SaveFormat) -> None:
        """Converts the pages of the specified input file to image files in the specified format.
        
        :param input_file: The input file name.
        :param output_file: The output file name used to generate file name for page images using rule "outputFile_pageIndex.extension"
        :param save_format: Save format. Only image save formats are allowed."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_file: str, output_file: str, save_options: aspose.words.saving.ImageSaveOptions) -> None:
        """Converts the pages of the specified input file to image files using the specified save options.
        
        :param input_file: The input file name.
        :param output_file: The output file name used to generate file name for page images using rule "outputFile_pageIndex.extension"
        :param save_options: Image save options."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_file: str, load_options: aspose.words.loading.LoadOptions, output_file: str, save_options: aspose.words.saving.ImageSaveOptions) -> None:
        """Converts the pages of the specified input file to image files using the provided load and save options.
        
        :param input_file: The input file name.
        :param load_options: The input document load options.
        :param output_file: The output file name used to generate file name for page images using rule "outputFile_pageIndex.extension"
        :param save_options: Image save options."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_file: str, save_format: aspose.words.SaveFormat) -> List[io.BytesIO]:
        """Converts the pages of the specified input file to images in the specified format and returns an array of streams containing the images.
        
        :param input_file: The input file name.
        :param save_format: Save format. Only image save formats are allowed.
        :returns: Returns array of image streams. The streams should be disposed by the end user."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_file: str, save_options: aspose.words.saving.ImageSaveOptions) -> List[io.BytesIO]:
        """Converts the pages of the specified input file to images using the specified save options and returns an array of streams containing the images.
        
        :param input_file: The input file name.
        :param save_options: Image save options.
        :returns: Returns array of image streams. The streams should be disposed by the end user."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_stream: io.BytesIO, save_format: aspose.words.SaveFormat) -> List[io.BytesIO]:
        """Converts the pages of the specified input stream to images in the specified format and returns an array of streams containing the images.
        
        :param input_stream: The input stream.
        :param save_format: Save format. Only image save formats are allowed.
        :returns: Returns array of image streams. The streams should be disposed by the end user."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_stream: io.BytesIO, save_options: aspose.words.saving.ImageSaveOptions) -> List[io.BytesIO]:
        """Converts the pages of the specified input stream to images using the specified save options and returns an array of streams containing the images.
        
        :param input_stream: The input stream.
        :param save_options: Image save options.
        :returns: Returns array of image streams. The streams should be disposed by the end user."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(input_stream: io.BytesIO, load_options: aspose.words.loading.LoadOptions, save_options: aspose.words.saving.ImageSaveOptions) -> List[io.BytesIO]:
        """Converts the pages of the specified input stream to images using the provided load and save options, and returns an array of streams containing the images.
        
        :param input_stream: The input stream.
        :param load_options: The input document load options.
        :param save_options: Image save options.
        :returns: Returns array of image streams. The streams should be disposed by the end user."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(doc: aspose.words.Document, save_format: aspose.words.SaveFormat) -> List[io.BytesIO]:
        """Converts the pages of the specified document to images in the specified format and returns an array of streams containing the images.
        
        :param doc: The input document.
        :param save_format: Save format. Only image save formats are allowed.
        :returns: Returns array of image streams. The streams should be disposed by the end user."""
        ...
    
    @overload
    @staticmethod
    def convert_to_images(doc: aspose.words.Document, save_options: aspose.words.saving.ImageSaveOptions) -> List[io.BytesIO]:
        """Converts the pages of the specified document to images using the specified save options and returns an array of streams containing the images.
        
        :param doc: The input document.
        :param save_options: Image save options.
        :returns: Returns array of image streams. The streams should be disposed by the end user."""
        ...
    
    ...

class MailMergeOptions:
    """Represents options for the mail merge functionality."""
    
    def __init__(self):
        ...
    
    @property
    def region_start_tag(self) -> str:
        """Gets or sets a mail merge region start tag."""
        ...
    
    @region_start_tag.setter
    def region_start_tag(self, value: str):
        ...
    
    @property
    def region_end_tag(self) -> str:
        """Gets or sets a mail merge region end tag."""
        ...
    
    @region_end_tag.setter
    def region_end_tag(self, value: str):
        ...
    
    @property
    def cleanup_options(self) -> aspose.words.mailmerging.MailMergeCleanupOptions:
        """Gets or sets a set of flags that specify what items should be removed during mail merge."""
        ...
    
    @cleanup_options.setter
    def cleanup_options(self, value: aspose.words.mailmerging.MailMergeCleanupOptions):
        ...
    
    @property
    def cleanup_paragraphs_with_punctuation_marks(self) -> bool:
        """Gets or sets a value indicating whether paragraphs with punctuation marks are considered as empty
        and should be removed if the :attr:`aspose.words.mailmerging.MailMergeCleanupOptions.REMOVE_EMPTY_PARAGRAPHS` option is specified.
        
        The default value is ``True``.
        
        Here is the complete list of cleanable punctuation marks:
        
        * !
        
        * ,
        
        * .
        
        * :
        
        * ;
        
        * ?
        
        * ¡
        
        * ¿"""
        ...
    
    @cleanup_paragraphs_with_punctuation_marks.setter
    def cleanup_paragraphs_with_punctuation_marks(self, value: bool):
        ...
    
    @property
    def use_non_merge_fields(self) -> bool:
        """When ``True``, specifies that in addition to MERGEFIELD fields, mail merge is performed into some other types of fields and
        also into "{{fieldName}}" tags.
        
        Normally, mail merge is only performed into MERGEFIELD fields, but several customers had their reporting
        built using other fields and had many documents created this way. To simplify migration (and because this
        approach was independently used by several customers) the ability to mail merge into other fields was introduced.
        
        When :attr:`MailMergeOptions.use_non_merge_fields` is set to ``True``, Aspose.Words will perform mail merge into the following fields:
        
        MERGEFIELD FieldName
        
        MACROBUTTON NOMACRO FieldName
        
        IF 0 = 0 "{FieldName}" ""
        
        Also, when :attr:`MailMergeOptions.use_non_merge_fields` is set to ``True``, Aspose.Words will perform mail merge into text tags
        "{{fieldName}}". These are not fields, but just text tags."""
        ...
    
    @use_non_merge_fields.setter
    def use_non_merge_fields(self, value: bool):
        ...
    
    @property
    def preserve_unused_tags(self) -> bool:
        """Gets or sets a value indicating whether the unused "mustache" tags should be preserved.
        
        The default value is ``False``."""
        ...
    
    @preserve_unused_tags.setter
    def preserve_unused_tags(self, value: bool):
        ...
    
    @property
    def merge_duplicate_regions(self) -> bool:
        """Gets or sets a value indicating whether all of the document mail merge regions with the name of a data source
        should be merged while executing of a mail merge with regions against the data source or just the first one.
        
        The default value is ``False``."""
        ...
    
    @merge_duplicate_regions.setter
    def merge_duplicate_regions(self, value: bool):
        ...
    
    @property
    def merge_whole_document(self) -> bool:
        """Gets or sets a value indicating whether fields in whole document are updated while executing of a mail merge with regions.
        
        The default value is ``False``."""
        ...
    
    @merge_whole_document.setter
    def merge_whole_document(self, value: bool):
        ...
    
    @property
    def use_whole_paragraph_as_region(self) -> bool:
        """Gets or sets a value indicating whether whole paragraph with **TableStart** or **TableEnd** field
        or particular range between **TableStart** and **TableEnd** fields should be included into mail merge region.
        
        The default value is ``True``."""
        ...
    
    @use_whole_paragraph_as_region.setter
    def use_whole_paragraph_as_region(self, value: bool):
        ...
    
    @property
    def restart_lists_at_each_section(self) -> bool:
        """Gets or sets a value indicating whether lists are restarted at each section after executing of a mail merge.
        
        The default value is ``True``."""
        ...
    
    @restart_lists_at_each_section.setter
    def restart_lists_at_each_section(self, value: bool):
        ...
    
    @property
    def trim_whitespaces(self) -> bool:
        """Gets or sets a value indicating whether trailing and leading whitespaces are trimmed from mail merge values.
        
        The default value is ``True``."""
        ...
    
    @trim_whitespaces.setter
    def trim_whitespaces(self, value: bool):
        ...
    
    @property
    def unconditional_merge_fields_and_regions(self) -> bool:
        """Gets or sets a value indicating whether merge fields and merge regions are merged regardless of the parent IF field's condition.
        
        The default value is ``False``."""
        ...
    
    @unconditional_merge_fields_and_regions.setter
    def unconditional_merge_fields_and_regions(self, value: bool):
        ...
    
    @property
    def retain_first_section_start(self) -> bool:
        """Gets or sets a value indicating whether the section start of the first document section and its copies for subsequent data source rows
        are retained during mail merge or updated according to MS Word behaviour.
        
        The default value is ``True``."""
        ...
    
    @retain_first_section_start.setter
    def retain_first_section_start(self, value: bool):
        ...
    
    ...

class MailMerger:
    """Provides methods intended to fill template with data using simple mail merge and mail merge with regions operations."""
    
    @overload
    @staticmethod
    def execute(input_file_name: str, output_file_name: str, field_names: List[str], field_values: List[object]) -> None:
        """Performs a mail merge operation for a single record.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param field_names: Array of merge field names. Field names are not case sensitive. If a field name that is not found in the document is encountered, it is ignored.
        :param field_values: Array of values to be inserted into the merge fields. Number of elements in this array must be the same as the number of elements in fieldNames."""
        ...
    
    @overload
    @staticmethod
    def execute(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, field_names: List[str], field_values: List[object]) -> None:
        """Performs a mail merge operation for a single record.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The output's save format.
        :param field_names: Array of merge field names. Field names are not case sensitive. If a field name that is not found in the document is encountered, it is ignored.
        :param field_values: Array of values to be inserted into the merge fields. Number of elements in this array must be the same as the number of elements in fieldNames."""
        ...
    
    @overload
    @staticmethod
    def execute(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, mail_merge_options: aspose.words.lowcode.MailMergeOptions, field_names: List[str], field_values: List[object]) -> None:
        """Performs a mail merge operation for a single record.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The output's save format.
        :param mail_merge_options: Mail merge options.
        :param field_names: Array of merge field names. Field names are not case sensitive. If a field name that is not found in the document is encountered, it is ignored.
        :param field_values: Array of values to be inserted into the merge fields. Number of elements in this array must be the same as the number of elements in fieldNames."""
        ...
    
    @overload
    @staticmethod
    def execute(input_file_name: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions, mail_merge_options: aspose.words.lowcode.MailMergeOptions, field_names: List[str], field_values: List[object]) -> None:
        """Performs a mail merge operation for a single record.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_options: The output's save options.
        :param mail_merge_options: Mail merge options.
        :param field_names: Array of merge field names. Field names are not case sensitive. If a field name that is not found in the document is encountered, it is ignored.
        :param field_values: Array of values to be inserted into the merge fields. Number of elements in this array must be the same as the number of elements in fieldNames."""
        ...
    
    @overload
    @staticmethod
    def execute(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, field_names: List[str], field_values: List[object]) -> None:
        """Performs a mail merge operation for a single record.
        
        :param input_stream: The input file stream.
        :param output_stream: The output file stream.
        :param save_format: The output's save format.
        :param field_names: Array of merge field names. Field names are not case sensitive. If a field name that is not found in the document is encountered, it is ignored.
        :param field_values: Array of values to be inserted into the merge fields. Number of elements in this array must be the same as the number of elements in fieldNames."""
        ...
    
    @overload
    @staticmethod
    def execute(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, mail_merge_options: aspose.words.lowcode.MailMergeOptions, field_names: List[str], field_values: List[object]) -> None:
        """Performs a mail merge operation for a single record.
        
        :param input_stream: The input file stream.
        :param output_stream: The output file stream.
        :param save_format: The output's save format.
        :param mail_merge_options: Mail merge options.
        :param field_names: Array of merge field names. Field names are not case sensitive. If a field name that is not found in the document is encountered, it is ignored.
        :param field_values: Array of values to be inserted into the merge fields. Number of elements in this array must be the same as the number of elements in fieldNames."""
        ...
    
    @overload
    @staticmethod
    def execute(input_stream: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions, mail_merge_options: aspose.words.lowcode.MailMergeOptions, field_names: List[str], field_values: List[object]) -> None:
        """Performs a mail merge operation for a single record.
        
        :param input_stream: The input file stream.
        :param output_stream: The output file stream.
        :param save_options: The output's save options.
        :param mail_merge_options: Mail merge options.
        :param field_names: Array of merge field names. Field names are not case sensitive. If a field name that is not found in the document is encountered, it is ignored.
        :param field_values: Array of values to be inserted into the merge fields. Number of elements in this array must be the same as the number of elements in fieldNames."""
        ...
    
    ...

class Merger:
    """Represents a group of methods intended to merge a variety of different types of documents into a single output document.
    
    The specified input and output files or streams, along with the desired merge and save options,
    are used to merge the given input documents into a single output document.
    
    The merging functionality supports over 35 different file formats."""
    
    @overload
    @staticmethod
    def merge(output_file: str, input_files: List[str]) -> None:
        """Merges the given input documents into a single output document using specified input and output file names.
        
        :param output_file: The output file name.
        :param input_files: The input file names.
        
        By default :attr:`MergeFormatMode.KEEP_SOURCE_FORMATTING` is used."""
        ...
    
    @overload
    @staticmethod
    def merge(output_file: str, input_files: List[str], save_format: aspose.words.SaveFormat, merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> None:
        """Merges the given input documents into a single output document using specified input output file names and the final document format.
        
        :param output_file: The output file name.
        :param input_files: The input file names.
        :param save_format: The save format.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge(output_file: str, input_files: List[str], save_options: aspose.words.saving.SaveOptions, merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> None:
        """Merges the given input documents into a single output document using specified input output file names and save options.
        
        :param output_file: The output file name.
        :param input_files: The input file names.
        :param save_options: The save options.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge(output_file: str, input_files: List[str], load_options: List[aspose.words.loading.LoadOptions], save_options: aspose.words.saving.SaveOptions, merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> None:
        """Merges the given input documents into a single output document using specified input output file names and save options.
        
        :param output_file: The output file name.
        :param input_files: The input file names.
        :param load_options: Load options for the input files.
        :param save_options: The save options.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge(input_files: List[str], merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> aspose.words.Document:
        """Merges the given input documents into a single document and returns :class:`aspose.words.Document` instance of the final document.
        
        :param input_files: The input file names.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge(input_files: List[str], load_options: List[aspose.words.loading.LoadOptions], merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> aspose.words.Document:
        """Merges the given input documents into a single document and returns :class:`aspose.words.Document` instance of the final document.
        
        :param input_files: The input file names.
        :param load_options: Load options for the input files.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge_stream(input_streams: List[io.BytesIO], merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> aspose.words.Document:
        """Merges the given input documents into a single document and returns :class:`aspose.words.Document` instance of the final document.
        
        :param input_streams: The input streams.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge_stream(output_stream: io.BytesIO, input_streams: List[io.BytesIO], save_format: aspose.words.SaveFormat) -> None:
        """Merges the given input documents into a single output document using specified input output streams and the final document format.
        
        :param output_stream: The output stream.
        :param input_streams: The input streams.
        :param save_format: The save format."""
        ...
    
    @overload
    @staticmethod
    def merge_stream(output_stream: io.BytesIO, input_streams: List[io.BytesIO], save_options: aspose.words.saving.SaveOptions, merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> None:
        """Merges the given input documents into a single output document using specified input output streams and save options.
        
        :param output_stream: The output stream.
        :param input_streams: The input streams.
        :param save_options: The save options.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @overload
    @staticmethod
    def merge_stream(output_stream: io.BytesIO, input_streams: List[io.BytesIO], load_options: List[aspose.words.loading.LoadOptions], save_options: aspose.words.saving.SaveOptions, merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> None:
        """Merges the given input documents into a single output document using specified input output streams and save options.
        
        :param output_stream: The output stream.
        :param input_streams: The input streams.
        :param load_options: Load options for the input files.
        :param save_options: The save options.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    @staticmethod
    def merge_docs(input_documents: List[aspose.words.Document], merge_format_mode: aspose.words.lowcode.MergeFormatMode) -> aspose.words.Document:
        """Merges the given input documents into a single document and returns :class:`aspose.words.Document` instance of the final document.
        
        :param input_documents: The input documents.
        :param merge_format_mode: Specifies how to merge formatting that clashes."""
        ...
    
    ...

class Replacer:
    """Provides methods intended to find and replace text in the document."""
    
    @overload
    @staticmethod
    def replace(input_file_name: str, output_file_name: str, pattern: str, replacement: str) -> int:
        """Replaces all occurrences of a specified character string pattern with a replacement string in the input file.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param pattern: A string to be replaced.
        :param replacement: A string to replace all occurrences of pattern.
        :returns: The number of replacements made."""
        ...
    
    @overload
    @staticmethod
    def replace(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, pattern: str, replacement: str) -> int:
        """Replaces all occurrences of a specified character string pattern with a replacement string in the input file, with the specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The save format.
        :param pattern: A string to be replaced.
        :param replacement: A string to replace all occurrences of pattern.
        :returns: The number of replacements made."""
        ...
    
    @overload
    @staticmethod
    def replace(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, pattern: str, replacement: str, options: aspose.words.replacing.FindReplaceOptions) -> int:
        """Replaces all occurrences of a specified character string pattern with a replacement string in the input file, with the specified save format and additional options.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The save format.
        :param pattern: A string to be replaced.
        :param replacement: A string to replace all occurrences of pattern.
        :param options: :class:`aspose.words.replacing.FindReplaceOptions` object to specify additional options.
        :returns: The number of replacements made."""
        ...
    
    @overload
    @staticmethod
    def replace(input_file_name: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions, pattern: str, replacement: str, options: aspose.words.replacing.FindReplaceOptions) -> int:
        """Replaces all occurrences of a specified character string pattern with a replacement string in the input file, with the specified save format and additional options.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_options: The save options.
        :param pattern: A string to be replaced.
        :param replacement: A string to replace all occurrences of pattern.
        :param options: :class:`aspose.words.replacing.FindReplaceOptions` object to specify additional options.
        :returns: The number of replacements made."""
        ...
    
    @overload
    @staticmethod
    def replace(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, pattern: str, replacement: str) -> int:
        """Replaces all occurrences of a specified character string pattern with a replacement string in the input stream, with the specified save format.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_format: The save format.
        :param pattern: A string to be replaced.
        :param replacement: A string to replace all occurrences of pattern.
        :returns: The number of replacements made."""
        ...
    
    @overload
    @staticmethod
    def replace(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, pattern: str, replacement: str, options: aspose.words.replacing.FindReplaceOptions) -> int:
        """Replaces all occurrences of a specified character string pattern with a replacement string in the input stream, with the specified save format and additional options.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_format: The save format.
        :param pattern: A string to be replaced.
        :param replacement: A string to replace all occurrences of pattern.
        :param options: :class:`aspose.words.replacing.FindReplaceOptions` object to specify additional options.
        :returns: The number of replacements made."""
        ...
    
    @overload
    @staticmethod
    def replace(input_stream: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions, pattern: str, replacement: str, options: aspose.words.replacing.FindReplaceOptions) -> int:
        """Replaces all occurrences of a specified character string pattern with a replacement string in the input stream, with the specified save format and additional options.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_options: The save options.
        :param pattern: A string to be replaced.
        :param replacement: A string to replace all occurrences of pattern.
        :param options: :class:`aspose.words.replacing.FindReplaceOptions` object to specify additional options.
        :returns: The number of replacements made."""
        ...
    
    ...

class ReportBuilder:
    """Provides methods intended to fill template with data using LINQ Reporting Engine."""
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, data: object) -> None:
        """Populates the template document with data from the specified source, generating a completed report.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param data: A data source object."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, data: object, report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from the specified source, generating a completed report with additional options.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param data: A data source object.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, data: object) -> None:
        """Populates the template document with data from the specified source, generating a completed report with specified output format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The output's save format.
        :param data: A data source object."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, data: object, report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from the specified source, generating a completed report with specified output format and additional options.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The output's save format.
        :param data: A data source object.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions, data: object, report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from the specified source, generating a completed report with specified output format and additional options.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_options: The output's save options.
        :param data: A data source object.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, data: object) -> None:
        """Populates the template document with data from the specified source, generating a completed report from input and output streams.
        
        :param input_stream: The input file stream.
        :param output_stream: The output file stream.
        :param save_format: The output's save format.
        :param data: A data source object."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, data: object, report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from the specified source, generating a completed report with specified output format and additional options, from input and output streams.
        
        :param input_stream: The input file stream.
        :param output_stream: The output file stream.
        :param save_format: The output's save format.
        :param data: A data source object.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_stream: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions, data: object, report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from the specified source, generating a completed report with specified output format and additional options, from input and output streams.
        
        :param input_stream: The input file stream.
        :param output_stream: The output file stream.
        :param save_options: The output's save options.
        :param data: A data source object.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, data: object, data_source_name: str) -> None:
        """Populates the template document with data from the specified source, generating a completed report with a named data source reference.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param data: A data source object.
        :param data_source_name: A name to reference the data source object in the template."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, data: object, data_source_name: str, report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from the specified source, generating a completed report with a named data source reference and additional options.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param data: A data source object.
        :param data_source_name: A name to reference the data source object in the template.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, data: object, data_source_name: str) -> None:
        """Populates the template document with data from the specified source, generating a completed report with specified output format and a named data source reference.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The output's save format.
        :param data: A data source object.
        :param data_source_name: A name to reference the data source object in the template."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, data: object, data_source_name: str, report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from the specified source, generating a completed report with specified output format, a named data source reference, and additional options.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The output's save format.
        :param data: A data source object.
        :param data_source_name: A name to reference the data source object in the template.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions, data: object, data_source_name: str, report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from the specified source, generating a completed report with specified output format, a named data source reference, and additional options.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_options: The output's save options.
        :param data: A data source object.
        :param data_source_name: A name to reference the data source object in the template.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, data: object, data_source_name: str) -> None:
        """Populates the template document with data from the specified source, generating a completed report with a named data source reference.
        
        :param input_stream: The input file stream.
        :param output_stream: The output file stream.
        :param save_format: The output's save format.
        :param data: A data source object.
        :param data_source_name: A name to reference the data source object in the template."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, data: object, data_source_name: str, report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from the specified source, generating a completed report with a named data source reference and additional options.
        
        :param input_stream: The input file stream.
        :param output_stream: The output file stream.
        :param save_format: The output's save format.
        :param data: A data source object.
        :param data_source_name: A name to reference the data source object in the template.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_stream: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions, data: object, data_source_name: str, report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from the specified source, generating a completed report with a named data source reference and additional options.
        
        :param input_stream: The input file stream.
        :param output_stream: The output file stream.
        :param save_options: The output's save options.
        :param data: A data source object.
        :param data_source_name: A name to reference the data source object in the template.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, data: List[object], data_source_names: List[str]) -> None:
        """Populates the template document with data from multiple sources, generating a completed report from the specified input and output file names.
        This overload automatically determines the save format based on the output file extension.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param data: An array of data source objects.
        :param data_source_names: An array of names to reference the data source objects within the template."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, data: List[object], data_source_names: List[str], report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from multiple sources, generating a completed report with additional options.
        This overload automatically determines the save format based on the output file extension.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param data: An array of data source objects.
        :param data_source_names: An array of names to reference the data source objects within the template.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, data: List[object], data_source_names: List[str]) -> None:
        """Populates the template document with data from multiple sources, generating a completed report with a specified output format.
        This overload automatically determines the save format based on the output file extension.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The output's save format.
        :param data: An array of data source objects.
        :param data_source_names: An array of names to reference the data source objects within the template."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, data: List[object], data_source_names: List[str], report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from multiple sources, generating a completed report with a specified output format and additional options.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The output's save format.
        :param data: An array of data source objects.
        :param data_source_names: An array of names to reference the data source objects within the template.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_file_name: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions, data: List[object], data_source_names: List[str], report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from multiple sources, generating a completed report with a specified output format and additional options.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_options: The output's save options.
        :param data: An array of data source objects.
        :param data_source_names: An array of names to reference the data source objects within the template.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, data: List[object], data_source_names: List[str]) -> None:
        """Populates the template document with data from multiple sources, generating a completed report from the specified input and output file streams.
        
        :param input_stream: The input file stream.
        :param output_stream: The output file stream.
        :param save_format: The output's save format.
        :param data: An array of data source objects.
        :param data_source_names: An array of names to reference the data source objects within the template."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, data: List[object], data_source_names: List[str], report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from multiple sources, generating a completed report with specified output format and additional options from the specified input and output file streams.
        
        :param input_stream: The input file stream.
        :param output_stream: The output file stream.
        :param save_format: The output's save format.
        :param data: An array of data source objects.
        :param data_source_names: An array of names to reference the data source objects within the template.
        :param report_builder_options: Additional report build options."""
        ...
    
    @overload
    @staticmethod
    def build_report(input_stream: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions, data: List[object], data_source_names: List[str], report_builder_options: aspose.words.lowcode.ReportBuilderOptions) -> None:
        """Populates the template document with data from multiple sources, generating a completed report with specified output format and additional options from the specified input and output file streams.
        
        :param input_stream: The input file stream.
        :param output_stream: The output file stream.
        :param save_options: The output's save options.
        :param data: An array of data source objects.
        :param data_source_names: An array of names to reference the data source objects within the template.
        :param report_builder_options: Additional report build options."""
        ...
    
    ...

class ReportBuilderOptions:
    """Represents options for the LINQ Reporting Engine functionality."""
    
    def __init__(self):
        ...
    
    @property
    def options(self) -> aspose.words.reporting.ReportBuildOptions:
        """Gets or sets a set of flags controlling behavior of this :class:`aspose.words.reporting.ReportingEngine` instance
        while building a report."""
        ...
    
    @options.setter
    def options(self, value: aspose.words.reporting.ReportBuildOptions):
        ...
    
    @property
    def missing_member_message(self) -> str:
        """Gets or sets a string value printed instead of a template expression that represents a plain reference to
        a missing member of an object. The default value is an empty string.
        
        The property should be used in conjunction with the :attr:`aspose.words.reporting.ReportBuildOptions.ALLOW_MISSING_MEMBERS`
        option. Otherwise, an exception is thrown when a missing member of an object is encountered.
        
        The property affects only printing of a template expression representing a plain reference to a missing
        object member. For example, printing of a binary operator, one of which operands references a missing
        object member, is not affected.
        
        The value of this property cannot be set to null."""
        ...
    
    @missing_member_message.setter
    def missing_member_message(self, value: str):
        ...
    
    @property
    def known_types(self) -> aspose.words.reporting.KnownTypeSet:
        """Gets an unordered set (i.e. a collection of unique items) containing  objects
        which fully or partially qualified names can be used within report templates processed by this engine
        instance to invoke the corresponding types' static members, perform type casts, etc."""
        ...
    
    ...

class SplitOptions:
    """Specifies options how the document is split into parts."""
    
    def __init__(self):
        ...
    
    @property
    def split_criteria(self) -> aspose.words.lowcode.SplitCriteria:
        """Specifies the criteria for splitting the document into parts."""
        ...
    
    @split_criteria.setter
    def split_criteria(self, value: aspose.words.lowcode.SplitCriteria):
        ...
    
    @property
    def split_style(self) -> str:
        """Specifies the paragraph style for splitting the document into parts when :attr:`SplitCriteria.STYLE` is used."""
        ...
    
    @split_style.setter
    def split_style(self, value: str):
        ...
    
    ...

class Splitter:
    """Provides methods intended to split the documents into parts using different criteria."""
    
    @overload
    @staticmethod
    def remove_blank_pages(input_file_name: str, output_file_name: str) -> None:
        """Removes empty pages from the document and saves the output. Returns a list of page numbers that were removed.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :returns: List of page numbers has been considered as blank and removed."""
        ...
    
    @overload
    @staticmethod
    def remove_blank_pages(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat) -> None:
        """Removes empty pages from the document and saves the output in the specified format. Returns a list of page numbers that were removed.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The save format.
        :returns: List of page numbers has been considered as blank and removed."""
        ...
    
    @overload
    @staticmethod
    def remove_blank_pages(input_file_name: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions) -> None:
        """Removes empty pages from the document and saves the output in the specified format. Returns a list of page numbers that were removed.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_options: The save options.
        :returns: List of page numbers has been considered as blank and removed."""
        ...
    
    @overload
    @staticmethod
    def remove_blank_pages(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat) -> None:
        """Removes blank pages from a document provided in an input stream and saves the updated document
        to an output stream in the specified save format. Returns a list of page numbers that were removed.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_format: The save format.
        :returns: List of page numbers has been considered as blank and removed."""
        ...
    
    @overload
    @staticmethod
    def remove_blank_pages(input_stream: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions) -> None:
        """Removes blank pages from a document provided in an input stream and saves the updated document
        to an output stream in the specified save format. Returns a list of page numbers that were removed.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_options: The save options.
        :returns: List of page numbers has been considered as blank and removed."""
        ...
    
    @overload
    @staticmethod
    def extract_pages(input_file_name: str, output_file_name: str, start_page_index: int, page_count: int) -> None:
        """Extracts a specified range of pages from a document file and saves the extracted pages
        to a new file. The output file format is determined by the extension of the output file name.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param start_page_index: The zero-based index of the first page to extract.
        :param page_count: Number of pages to be extracted."""
        ...
    
    @overload
    @staticmethod
    def extract_pages(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, start_page_index: int, page_count: int) -> None:
        """Extracts a specified range of pages from a document file and saves the extracted pages
        to a new file using the specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The save format.
        :param start_page_index: The zero-based index of the first page to extract.
        :param page_count: Number of pages to be extracted."""
        ...
    
    @overload
    @staticmethod
    def extract_pages(input_file_name: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions, start_page_index: int, page_count: int) -> None:
        """Extracts a specified range of pages from a document file and saves the extracted pages
        to a new file using the specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_options: The save options.
        :param start_page_index: The zero-based index of the first page to extract.
        :param page_count: Number of pages to be extracted."""
        ...
    
    @overload
    @staticmethod
    def extract_pages(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, start_page_index: int, page_count: int) -> None:
        """Extracts a specified range of pages from a document stream and saves the extracted pages
        to an output stream using the specified save format.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_format: The save format.
        :param start_page_index: The zero-based index of the first page to extract.
        :param page_count: Number of pages to be extracted."""
        ...
    
    @overload
    @staticmethod
    def extract_pages(input_stream: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions, start_page_index: int, page_count: int) -> None:
        """Extracts a specified range of pages from a document stream and saves the extracted pages
        to an output stream using the specified save format.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_options: The save options.
        :param start_page_index: The zero-based index of the first page to extract.
        :param page_count: Number of pages to be extracted."""
        ...
    
    @overload
    @staticmethod
    def split(input_file_name: str, output_file_name: str, options: aspose.words.lowcode.SplitOptions) -> None:
        """Splits a document into multiple parts based on the specified split options and saves
        the resulting parts to files. The output file format is determined by the extension of the output file name.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name used to generate file name for document parts using rule "outputFile_partIndex.extension"
        :param options: Document split options."""
        ...
    
    @overload
    @staticmethod
    def split(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, options: aspose.words.lowcode.SplitOptions) -> None:
        """Splits a document into multiple parts based on the specified split options and saves
        the resulting parts to files in the specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name used to generate file name for document parts using rule "outputFile_partIndex.extension"
        :param save_format: The save format.
        :param options: Document split options."""
        ...
    
    @overload
    @staticmethod
    def split(input_file_name: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions, options: aspose.words.lowcode.SplitOptions) -> None:
        """Splits a document into multiple parts based on the specified split options and saves
        the resulting parts to files in the specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name used to generate file name for document parts using rule "outputFile_partIndex.extension"
        :param save_options: The save options.
        :param options: Document split options."""
        ...
    
    @overload
    @staticmethod
    def split(input_stream: io.BytesIO, save_format: aspose.words.SaveFormat, options: aspose.words.lowcode.SplitOptions) -> List[io.BytesIO]:
        """Splits a document from an input stream into multiple parts based on the specified split options and
        returns the resulting parts as an array of streams in the specified save format.
        
        :param input_stream: The input stream.
        :param save_format: The save format.
        :param options: Document split options."""
        ...
    
    @overload
    @staticmethod
    def split(input_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions, options: aspose.words.lowcode.SplitOptions) -> List[io.BytesIO]:
        """Splits a document from an input stream into multiple parts based on the specified split options and
        returns the resulting parts as an array of streams in the specified save format.
        
        :param input_stream: The input stream.
        :param save_options: The save options.
        :param options: Document split options."""
        ...
    
    ...

class Watermarker:
    """Provides methods intended to insert watermarks into the documents."""
    
    @overload
    @staticmethod
    def set_text(input_file_name: str, output_file_name: str, watermark_text: str) -> None:
        """Adds a text watermark into the document.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param watermark_text: Text that is displayed as a watermark."""
        ...
    
    @overload
    @staticmethod
    def set_text(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, watermark_text: str) -> None:
        """Adds a text watermark into the document with specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The save format.
        :param watermark_text: Text that is displayed as a watermark."""
        ...
    
    @overload
    @staticmethod
    def set_text(input_file_name: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions, watermark_text: str) -> None:
        """Adds a text watermark into the document with specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_options: The save options.
        :param watermark_text: Text that is displayed as a watermark."""
        ...
    
    @overload
    @staticmethod
    def set_text(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, watermark_text: str) -> None:
        """Adds a text watermark into the document from streams.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_format: The save format.
        :param watermark_text: Text that is displayed as a watermark."""
        ...
    
    @overload
    @staticmethod
    def set_text(input_stream: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions, watermark_text: str) -> None:
        """Adds a text watermark into the document from streams.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_options: The save options.
        :param watermark_text: Text that is displayed as a watermark."""
        ...
    
    @overload
    @staticmethod
    def set_text(input_file_name: str, output_file_name: str, watermark_text: str, options: aspose.words.TextWatermarkOptions) -> None:
        """Adds a text watermark into the document with options.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param watermark_text: Text that is displayed as a watermark.
        :param options: Defines additional options for the text watermark."""
        ...
    
    @overload
    @staticmethod
    def set_text(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, watermark_text: str, options: aspose.words.TextWatermarkOptions) -> None:
        """Adds a text watermark into the document with options and specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The save format.
        :param watermark_text: Text that is displayed as a watermark.
        :param options: Defines additional options for the text watermark."""
        ...
    
    @overload
    @staticmethod
    def set_text(input_file_name: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions, watermark_text: str, options: aspose.words.TextWatermarkOptions) -> None:
        """Adds a text watermark into the document with options and specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_options: The save options.
        :param watermark_text: Text that is displayed as a watermark.
        :param options: Defines additional options for the text watermark."""
        ...
    
    @overload
    @staticmethod
    def set_text(input_stream: io.BytesIO, output_stream: io.BytesIO, save_format: aspose.words.SaveFormat, watermark_text: str, options: aspose.words.TextWatermarkOptions) -> None:
        """Adds a text watermark into the document from streams with options.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_format: The save format.
        :param watermark_text: Text that is displayed as a watermark.
        :param options: Defines additional options for the text watermark."""
        ...
    
    @overload
    @staticmethod
    def set_text(input_stream: io.BytesIO, output_stream: io.BytesIO, save_options: aspose.words.saving.SaveOptions, watermark_text: str, options: aspose.words.TextWatermarkOptions) -> None:
        """Adds a text watermark into the document from streams with options.
        
        :param input_stream: The input stream.
        :param output_stream: The output stream.
        :param save_options: The save options.
        :param watermark_text: Text that is displayed as a watermark.
        :param options: Defines additional options for the text watermark."""
        ...
    
    @overload
    @staticmethod
    def set_image(input_file_name: str, output_file_name: str, watermark_image_file_name: str) -> None:
        """Adds an image watermark into the document.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param watermark_image_file_name: Image that is displayed as a watermark."""
        ...
    
    @overload
    @staticmethod
    def set_image(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, watermark_image_file_name: str) -> None:
        """Adds an image watermark into the document with specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The save format.
        :param watermark_image_file_name: Image that is displayed as a watermark."""
        ...
    
    @overload
    @staticmethod
    def set_image(input_file_name: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions, watermark_image_file_name: str) -> None:
        """Adds an image watermark into the document with specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_options: The save options.
        :param watermark_image_file_name: Image that is displayed as a watermark."""
        ...
    
    @overload
    @staticmethod
    def set_image(input_file_name: str, output_file_name: str, watermark_image_file_name: str, options: aspose.words.ImageWatermarkOptions) -> None:
        """Adds an image watermark into the document with options.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param watermark_image_file_name: Image that is displayed as a watermark.
        :param options: Defines additional options for the image watermark."""
        ...
    
    @overload
    @staticmethod
    def set_image(input_file_name: str, output_file_name: str, save_format: aspose.words.SaveFormat, watermark_image_file_name: str, options: aspose.words.ImageWatermarkOptions) -> None:
        """Adds an image watermark into the document with options and specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_format: The save format.
        :param watermark_image_file_name: Image that is displayed as a watermark.
        :param options: Defines additional options for the image watermark."""
        ...
    
    @overload
    @staticmethod
    def set_image(input_file_name: str, output_file_name: str, save_options: aspose.words.saving.SaveOptions, watermark_image_file_name: str, options: aspose.words.ImageWatermarkOptions) -> None:
        """Adds an image watermark into the document with options and specified save format.
        
        :param input_file_name: The input file name.
        :param output_file_name: The output file name.
        :param save_options: The save options.
        :param watermark_image_file_name: Image that is displayed as a watermark.
        :param options: Defines additional options for the image watermark."""
        ...
    
    ...

class MergeFormatMode(Enum):
    """Specifies how formatting is merged when combining multiple documents."""
    
    """Combine the formatting of the merged documents.
    
    By using this option, Aspose.Words adapts the formatting of the first document to match the structure and
    appearance of the second document, but keeps some of the original formatting intact.
    This option is useful when you want to maintain the overall look and feel of the destination document
    but still retain certain formatting aspects from the original document.
    
    This option does not have any affect when the input and the output formats are PDF."""
    MERGE_FORMATTING: int
    
    """Means that the source document will retain its original formatting,
    such as font styles, sizes, colors, indents, and any other formatting elements applied to its content.
    
    By using this option, you ensure that the copied content appears as it did in the original source,
    regardless of the formatting settings of the first document in merge queue.
    
    This option does not have any affect when the input and the output formats are PDF."""
    KEEP_SOURCE_FORMATTING: int
    
    """Preserve the layout of the original documents in the final document.
    
    In general, it looks like you print out the original documents and manually adhere them together using glue."""
    KEEP_SOURCE_LAYOUT: int
    

class SplitCriteria(Enum):
    """Specifies how the document is split into parts."""
    
    """Specifies that the document is split into pages."""
    PAGE: int
    
    """Specifies that the document is split into parts at a section break of any type."""
    SECTION_BREAK: int
    
    """Specifies that the document is split into parts at a paragraph formatted using the style specified in :attr:`SplitOptions.split_style`."""
    STYLE: int
    

