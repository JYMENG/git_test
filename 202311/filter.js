transformData() {
  this.jsonData = this.jsonData.map(item => _.mapKeys(item, (value, key) => this.columnRenameMapping[key] || key));
  this.jsonData = this.jsonData.map(item => _.pick(item, Object.values(this.columnRenameMapping)));
}
