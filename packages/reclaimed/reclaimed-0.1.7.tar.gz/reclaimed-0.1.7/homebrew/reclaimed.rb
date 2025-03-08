class Reclaimed < Formula
  include Language::Python::Virtualenv

  desc "A powerful disk usage analyzer with iCloud support"
  homepage "https://github.com/taylorwilsdon/reclaimed"
  version "0.1.6"
  url "https://github.com/taylorwilsdon/reclaimed/archive/refs/tags/v#{version}.tar.gz"
  sha256 "5baacc4076063c649a9f143182f1af9370fedcbef15de777da0a6782ce24839b" # Will be updated by release script
  license "MIT"

  depends_on "python@3.11"
  
  # Build dependencies
  resource "hatchling" do
    url "https://files.pythonhosted.org/packages/d8/a1/7dd1caa87c0b15c04c6291e25112e5d082cce02ee87f221a8be1d594f857/hatchling-1.21.1.tar.gz"
    sha256 "bba440453a224e7d4478457fa2e8d8c3633765bafa02975a6b53b9bf917980bc"
  end

  resource "hatch-vcs" do
    url "https://files.pythonhosted.org/packages/f5/c9/54bb4fa27b4e4a014ef3bb17710cdf692b3aa2cbc7953da885f1bf7e06ea/hatch_vcs-0.4.0.tar.gz"
    sha256 "093810748fe01db0d451fabcf2c1ac2688caefd232d4a5df9a14f08c74f79e9e"
  end

  resource "setuptools-scm" do
    url "https://files.pythonhosted.org/packages/eb/b1/0723c86210b12b4b6139eb6579b9242d1ea37b5883216bd0b11d562f429a/setuptools_scm-8.0.4.tar.gz"
    sha256 "b5f43ff6800669595706ee0eff077fe282b8c264e2f45c44dd20b016b56c0b17"
  end

  # Runtime dependencies
  resource "click" do
    url "https://files.pythonhosted.org/packages/96/d3/f04c7bfcf5c1862a2a5b845c6b2b360488cf47af55dfa79c98f6a6bf98b5/click-8.1.7.tar.gz"
    sha256 "ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de"
  end

  resource "rich" do
    url "https://files.pythonhosted.org/packages/a7/ec/4a7d80728bd429f7c0d4d51245287158a1516315cadbb146012439403a9d/rich-13.7.0.tar.gz"
    sha256 "5cb5123b5cf9ee70584244246816e9114227e0b98ad9176eede6ad54bf5403fa"
  end

  resource "textual" do
    url "https://files.pythonhosted.org/packages/bb/ce/b224ccc05260871da8df640e7cd8ca0a5e38721fddb6733650195402841e/textual-0.52.1.tar.gz"
    sha256 "4232e5c2b423ed7c63baaeb6030355e14e1de1b9df096c9655b68a1e60e4de5f"
  end

  def install
    # Set static version for build since we don't have git metadata in the tarball
    ENV["SETUPTOOLS_SCM_PRETEND_VERSION"] = version
    virtualenv_install_with_resources
  end

  test do
    system bin/"reclaimed", "--help"
  end
end
